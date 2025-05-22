# Kitting Area Visualization & Management Prototype
_Location: Huhtamaki Plant, Marion, Indiana_

## Project Overview
The goal is to develop a standalone prototype web application for the kitting area in the Marion plant. The kitting area consists of two shelves (each with 5 rows and 5 columns, top row unused) and 10 floor pallets for larger kits. Each kit corresponds to a maintenance project, PM, upgrade, or repair, and is stored in a black tote with a yellow lid, labeled with a kit number and work order.

The prototype will provide a visual representation of the shelves and pallets, allowing users to see at a glance which slots are empty or occupied, and interact with each kit for check-in/out, updates, and status changes. Data will be stored in an Oracle database, and the prototype will be built primarily with Python and SQL, using HTML/CSS for the initial UI.

### Physical Layout

#### Shelves:
* 2 shelves, each with 5 rows (Row 0 to Row 4; Row 0 is unused)
* 5 columns per shelf (10 columns total)
* Kit numbers 1–40 assigned to shelf slots (left to right, top to bottom, skipping Row 0)

**Shelf Layout (Top View, ASCII Art):**

```
Shelves (Rows 0-4, Columns 1-10)
[Row 0]  [  ][  ][  ][  ][  ][  ][  ][  ][  ][  ]   <- Unused
[Row 1]  [ 1][ 2][ 3][ 4][ 5][ 6][ 7][ 8][ 9][10]
[Row 2]  [11][12][13][14][15][16][17][18][19][20]
[Row 3]  [21][22][23][24][25][26][27][28][29][30]
[Row 4]  [31][32][33][34][35][36][37][38][39][40]
```

#### Floor Pallets:
* 10 pallets for Kits 41–50 (for larger jobs)

**Pallet Layout (Front View, ASCII Art):**

```
Floor Pallets:
[41][42][43][44][45][46][47][48][49][50]
```

---

### Visual Representation

* Each shelf slot or pallet is a box.
* Occupied slots show a black box with a yellow lid and a kit number.
* Empty slots are blank or gray.
* Status is shown by a colored dot or icon in the corner.

**Example Slot (ASCII):**

```
+-----+
|#12 ●|   #12 = Kit Number, ● = Status Indicator (color-coded)
|[██] |   ██ = Black tote, yellow lid (conceptual)
+-----+
```

---

### Status Indicator Legend

| Symbol | Status       | Color   | Meaning            |
|--------|--------------|---------|--------------------|
| 🟢     | Ready        | Green   | Kit is ready       |
| 🟡     | In Progress  | Yellow  | Being worked on    |
| 🔴     | Issue        | Red     | Needs attention    |
| 🔵     | Checked Out  | Blue    | Kit is in use      |
| ⚪     | Empty        | Gray    | Slot is empty      |

---

### Kit Management:
* Add new kit to a slot or pallet
* Remove kit from a slot or pallet
* Check out a kit (mark as in use)
* Add/remove items to/from a kit
* Edit kit details

### Kit Information:
* Store and display the following fields for each kit:
* Kit Number
* Work Order Number
* Project/PM/Repair/Upgrade type
* Assigned Technician(s)
* Due Date
* Status (Ready, In Progress, Complete, Issue, etc.)
* Parts List
* Notes/Comments

### Status Indicators:
* Use color-coded icons (e.g., green = ready, red = issue, yellow = in progress, blue = checked out, etc.) for quick status at a glance

### Data Storage:
* Use Oracle SQL for persistent storage
* Manual data entry for all fields (no integration with other systems at this stage)

### Technology Stack:
* Backend: Python (Flask or FastAPI)
* Frontend: HTML5/CSS for prototype, with plan to migrate to React or Vue.js
* Database: Oracle SQL (SQLite for early prototyping if needed)
* Visualization: Simple grid/diagram for shelf and pallet layout
* Development Approach

### Database Design:
* Define tables for kits, work orders, technicians, parts, and statuses
* Ensure relationships (foreign keys) between kits and work orders, assigned techs, etc.

### Backend API:
* Python-based API for CRUD operations on kits and related data

### Frontend UI:
* Initial static HTML/CSS grid for visualization
* Interactive elements for kit management
* Color-coded status indicators

### Functionality:
* Manual data entry and updates
* Visual feedback for kit status and location
* Ability to search/filter kits

#### Future Enhancements:
* Barcode scanning for kit/part entry
* Automated alerts for overdue kits
* Drag-and-drop UI for moving kits
* Integration with parts system (if approved)

## Notes
* The prototype is for functionality testing, not final appearance.
* All data entry will be manual; no network integration or automation at this stage.
* The system should be simple, robust, and easy to use for maintenance staff.