<p align="center">
  <img width="180" height="180" src="https://github.com/CharlieFuu69/RenPy_RhythmBeats/blob/main/icons/llup_icon.png">
</p>

<h2 align="center"> LoveLive! UNOFFICIAL PROJECT </h2>
<h5 align="center"> Roadmap (Development progress) </h5>

> [!NOTE]
> _This Roadmap may be subject to change due to delays, creation of new features and other elements not noted.._

---

### Summary:

| Last status update             | Completed tickets   | Pending tickets    | Total progress        |
|---|---|---|---|
| `2024-03-21 14:09 (GMT -3)`    | 129                 | 8                  | 44.44% (8/18 tareas)  |

---

### Feature checklist:

- [x] **[COMPLETE] REFURBISHING THE CORE OF "REN'PY RHYTHMBEATS!".**

- [x] **[COMPLETE] DISCORD RICH PRESENCE SERVICE INTEGRATION.**

- [x] **[COMPLETE] STORAGE OF MAIN PLAYER DATA.**

- [x] **[COMPLETE] SONG SELECTOR ("SINGLE PLAYER" MODE).**

- [x] **[COMPLETE] DISPLAYABLE CACHING SYSTEM (IMAGES/MVs).**

- [x] **[COMPLETE] PLAYER PROGRESS SYSTEM (PLAYER LEVEL).**

- [x] **[COMPLETE] PLAYER COLLECTION PANEL.**

- [x] **[COMPLETE] RECRUITMENT MENU (Gacha).**

- [ ] **[IN PROGRESS] START MENU.**
> - [x] Add system clock (Date and Time).
>   > - [x] Create `DynamicDisplayable()` to constantly update the clock.
>   > - [x] Show UTC (world) time by default.
>   > - [x] Add option in settings to choose between UTC (world) time and GMT (local time, auto-detected time zone).
>
> - [ ] Sprite of the selected favorite School Idol.
>   > - [ ] Create a School Idols selector.
>   > - [ ] Create essential animation for blinks.
>   > - [ ] Create adaptive displayables to support multiple expressions per sprite.


- [ ] **[WAITING] GAME SECTION: LIVE SHOWS.**
> - [x] Sequence of the Live Shows.
>   > - [x] Show cover art, title, Full Combo and BPM of the song to play.
>   > - [x] Instantiate the game as a Ren'Py RhythmBeats core object! (`RhythmPlayground()`).
>   > - [x] Show Live Show judgment at the end of the game (Live Cleared!, Full Combo!, All Perfect!).
>   > - [x] Show XP obtained by Live Show performance.
>   >   > - [x] XP for Live Show judgment.
>   >   > - [x] XP for average reaction time.
>   >   > - [x] XP for new record achieved.
>   >
>   > - [ ] Show results (statistics) of the Live Show.
>   >   > - [x] Number of notes Perfect!.
>   >   > - [x] Amount of notes Great!.
>   >   > - [x] Number of Miss notes.
>   >   > - [x] Show Full Combo/All Perfect flag.
>   >   > - [x] Show new record flag.
>   >   > - [x] Show PP obtained in the Live Show.
>   >   > - [x] Show the Rank of the Live Show (CBAS).
>   >   > - [ ] Show most dominant card (MVP) of the Live Show.
>   >   > - [ ] Choose and display Live Show reward items.


- [ ] **[WAITING] ASSETS MANAGER AND DOWNLOADS FROM THE CDN.**
> - [x] Check for updates by examining asset packages.
>   > - [x] Remove old hash storage system.
>   > - [x] Scan local files to compare CDN hash differences with the client.
>   > - [x] Stack files that are missing or require updates.
>   > - [x] Delete files from failed downloads (temporary).
>
> - [x] Modifications to the download display.
>   > - [x] Automatically convert Bytes to kB, MB and GB.
>   > - [x] Create a bandwidth meter for downloads (MB/s).
>   > - [x] Preformat download data (MB downloaded, totals, bandwidth, blocks downloaded and percentage).
>   >   > - [x] Format downloaded MB.
>   >   > - [x] Format total download size (MB).
>   >   > - [x] Format bandwidth meter.
>   >   > - [x] Format downloaded block counter.
>   >   > - [x] Format total download percentage.
>   >
>   > - [x] Predict images (load into RAM) of sprites in the download screen.
>
> - [ ] Create a Light download mode (only songs) and Full mode (songs + MVs)

- [ ] **[PENDING] LIVE SHOW TRAINING PANEL.**

- [ ] **[PENDING] AFFINITY PANEL WITH FAVORITE SCHOOL IDOL.**

- [ ] **[PENDING] MISSION PANEL WITH REWARDS.**

- [ ] **[PENDING] PLAYER PROFILE PANEL.**

- [ ] **[PENDING] PLAYER ACCOUNT SYSTEM (LoveLive Fan ID, Database).**

- [ ] **[PENDING] ASYNCHRONOUS ONLINE EVENTS (GAME MODES AND SERVER BACKEND).**

- [ ] **[PENDING] MAP A TOTAL OF 30 SONGS FOR RELEASE.**

- [ ] **[PENDING] RELEASE PROCEDURE FOR "LOVELIVE! UNOFFICIAL PROJECT".**
