## ✅ FileSwirl Feature Roadmap

A checklist of planned and suggested features to evolve FileSwirl into a smart, scalable, and distributed file organization system.

V2
---
### 🚀 Core Features

* [ ] **AutoScaler**

  * [ ] Dynamic thread/process pool adjustment based on load
  * [ ] Queue-based producer-consumer architecture
<br><br>
* [ ] **Distributed Sorting**

  * [ ] Connect multiple NAS or remote file sources
  * [ ] Use gRPC or ZeroMQ for communication
  * [ ] File syncing across machines
<br><br>
* [ ] **Fault Tolerance**

  * [ ] Resume on crash or disconnection
  * [ ] Journal file tracking for reliability
  * [ ] Retry failed transfers
<br><br>
* [ ] **ETA Estimation**

  * [ ] Show estimated completion time
  * [ ] Show live progress % and throughput (files/sec)
<br><br>
* [ ] **Mobile Device Sync**

  * [ ] MTP support for Android
  * [ ] WiFi/local sync with apps or WebDAV
<br><br>
* [ ] **Real-time Folder Watcher**

  * [ ] Watchdog (Windows/macOS/Linux)
  * [ ] fswatch / inotify / polling fallback
  * [ ] Automatically apply rules on new files
<br><br>

* [ ] **Organize by Location (DBSCAN)**

  * [ ] Parse GPS metadata (EXIF)
  * [ ] Group by geoclusters (e.g., cities, trips)
  * [ ] Sort images into location-based folders



V3
---

* [ ] **GUI Rule Builder**

  * [ ] Drag-and-drop logic builder
  * [ ] Set up filters for extension, size, date, GPS, etc.

* [ ] **Plugin/Rule System**

  * [ ] Allow user-defined Python or YAML rules
  * [ ] Hot-reload without restarting app

* [ ] **Multi-Destination Routing**

  * [ ] Route files to different folders based on rules
  * [ ] Example: Photos → `/Photos/2025/`, Docs → `/Documents/`

* [ ] **Deduplication**

  * [ ] SHA256-based deduplication
  * [ ] Optional perceptual hashing (for media)

* [ ] **Metadata Filtering**
  * [ ] PDF document metadata (author, title, etc.)

* [ ] **Web Dashboard**
  * [ ] View system status, logs, and queues
  * [ ] Live preview of sort results
  * [ ] Remote control (start/stop, dry run toggle)

---
