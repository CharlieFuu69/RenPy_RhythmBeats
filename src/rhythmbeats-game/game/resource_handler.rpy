## CharlieFuu69
## Ren'Py RhythmBeats! Game

## Script: Manipulador de recursos y descarga de paquetes.

## © 2023 CharlieFuu69 - GNU GPL v3.0

################################################################################

init python:
    import time, json, requests, threading, ssl

    class UpdateManager(threading.Thread):

        def __init__(self, ext = "", skip = True):
            """Constructor de la clase UpdateManager().
            Esta clase se encarga de realizar los procedimientos de recuperación de datos del
            host (ver atributo self.index_url), comprobar si existen actualizaciones y gestionar la
            descarga de paquetes necesarios para la ejecución del juego demostrativo."""

            super(UpdateManager, self).__init__()

            self.daemon = True

            self.index_url = None
            self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
                            "Accept-Encoding" : "identity"}

            self.dl_path = config.gamedir if any((renpy.windows, renpy.linux)) else os.path.join(os.environ["ANDROID_PUBLIC"], "game")
            self.ext = ext
            self.skip = skip

            self.local_index = persistent.local_index
            self.remote_index = dict()

            self.request_end = False
            self.exception_content = None

            self.update_queue = list()
            self.update_size = 0
            self.progress = [0, 0]


        def setup(self):
            """Este método prepara el entorno de administración y elimina archivos residuales
            de descargas fallidas o repetidas."""

            if not persistent.local_index:
                self.local_index = persistent.local_index = {}

            if not os.path.exists(self.dl_path):
                os.mkdir(self.dl_path)

            logging.info("Eliminando archivos residuales...")
            for file in os.listdir(self.dl_path):
                if file.endswith(("tmp", ")%s" % self.ext)):
                    os.remove(os.path.join(self.dl_path, file))

            logging.info("Archivos residuales eliminados.")


        def get_exception(self):
            """Este método retorna True si ocurrió una excepción durante el procedimiento
            de actualización. En el caso contrario, retorna False."""

            if isinstance(self.exception_content, Exception):
                return True
            return False


        def get_update(self):
            """Este método realiza la comparación de los índices del servidor con los índices
            locales para comprobar si se requiere actualizar o descargar nuevos paquetes.
            Al obtener la comparación, recupera los endpoints de los paquetes (Mediafire)
            y computa el tamaño total de descarga según el header recibido."""

            ssl._create_default_https_context = ssl._create_unverified_context

            current_queue = list()

            logging.info("Comparando índice local con el índice remoto")
            if not self.skip:
                print("--------------- COMPARE ---------------")
                for pkg in self.remote_index:
                    if pkg["name"] in self.local_index:
                        if pkg["md5"] != self.local_index[pkg["name"]] or not renpy.exists(pkg["name"] + self.ext):
                            if renpy.exists(pkg["name"] + self.ext):
                                os.remove(os.path.join(self.dl_path, pkg["name"] + self.ext))
                            current_queue.append(pkg)
                    else:
                        current_queue.append(pkg)
            else:
                logging.info("Comparación omitida. Modo desarrollador activo.")

            self.progress = [0, len(current_queue)]

            ## Adquisición de endpoints y tamaño de descarga
            if len(current_queue) > 0:
                logging.info("Obteniendo endpoints de descarga...")

                for pkg in current_queue:
                    self.progress[0] += 1

                    r = requests.head(pkg["url"], headers = self.headers, timeout = 5, allow_redirects = True)
                    self.update_size += round(float(r.headers["Content-Length"]) / 1048576.0, 2)
                    self.update_queue.append(pkg)
                    renpy.restart_interaction()


        def start_batch_download(self):
            """Este método realiza la descarga por lotes con la cola de archivos a descargar.
            La screen download() es llamada cada vez que se necesita descargar un archivo."""

            batch_length = len(self.update_queue)
            batch_count = 0

            logging.info("Descargando recursos...")
            logging.info("Cola de descarga esperada: %s" % batch_length)

            for pkg in sorted(self.update_queue):
                logging.info("Descargando \"%s\"..." % pkg["name"])
                batch_count += 1

                renpy.call_screen("download",
                            url = pkg["url"],
                            progress = (batch_count, batch_length),
                            path = os.path.join(self.dl_path, pkg["name"] + self.ext))

                self.update_queue.remove(pkg)
                persistent.local_index.update({pkg["name"] : pkg["md5"]})


        def run(self):
            """Este método ejecuta la búsqueda de actualizaciones en un hilo paralelo al del juego
            mediante threading.Thread."""

            remote_ver = None

            self.setup()

            try:
                logging.info("Recuperando índice remoto...")
                r = requests.get(self.index_url, timeout = 5)

                if r.status_code == 200:
                    index_digest = json.loads(r.text)

                    self.remote_index = index_digest["packages"]
                    remote_ver = index_digest["version"]

                    logging.info("Comprobando versión global...")
                    if remote_ver != config.version:
                        renpy.call_screen("need_main_update", now_version = remote_ver)

                    self.get_update()
                else:
                    raise Exception("Error de adquisición de datos: %s" % r)

            except Exception as update_error:
                self.exception_content = update_error
                logging.error(str(update_error))

            finally:
                self.request_end = True
                renpy.restart_interaction()
