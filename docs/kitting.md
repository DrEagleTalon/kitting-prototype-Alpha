Help me write a IT Seervice desk request to the company i work for (Huhtamaki) and my name and email are Yusuf Talan Saunders Yusuf.Saunders@Huhtamaki.com and i am a Controls Engineer here working on PLCs, networks, embedded devices, VFDs, data collection, etc. II just got my PC and while i have worked for Tyson doing Local Admin (LA Account) work deploying machines and doingedge IoT work i know that just cause i can doesnt mean ishould or get. I dont want LA or naything all i want is either for IT to install for me a list of reqiremnts in a .txt file or maybe a VM for a dev environment. For instance we have a kitting area for maintenance where maintenance qworkers have Preventative maintenance or project work planned and they go get a alrge black tote or pallet for larger sets and gets the parts ist for that job and gets them, checks them out, puts tjem in a binb and assigns it to a KIT # (Numbered 1-50) so when the job is ready to be done they can grab it and go. I have been tasked with creating a standalone, not on network, prototype for the kitting area for a visual representation of the racks and bins and wbe able to interact with it, get status of Kit, work order, techs assigned, date due, or add or remove kits, complete jobs, etc.  I plan to use VS Code (already installed on device) with python using various libraries like TKinter, and others, oracle sql database. im starting with HTML/CSS but will be transitioning to Vue/React i believe and will build itt from ground up anticipating that swap. So a simple website thats hosted on an internal network at a paper plate manufacturing plant and be a visual representation of their kitting area with the ability to check things in and out, look at it from a glance by seeing indicators/lights/etc to indicate certain statuses.
POSSIBLE TECH STACK (im open to suggestions but the simpler the better and python, ssql, javascript are the easiest for me)
- Frontend: Start with HTML/CSS for basic UI, then transition to Vue.js or React for a more dynamic interface.
- Backend: Python with Flask or FastAPI for lightweight API handling.
- Database: Oracle SQL for structured data storage.
- GUI: Tkinter for initial local UI development before moving to a web-based interface.
- Visualization: Use CanvasJS or D3.js for interactive rack/bin representations.
- Local Hosting: Since it’s not on a network, consider SQLite for early prototyping before integrating Oracle SQL.
Development Approach
- Database Design
- Define tables for kits, work orders, techs, parts inventory, and statuses.
- Ensure foreign keys link kits to work orders and assigned techs.
- Optimize queries for fast lookups (e.g., checking kit status).
- UI & Interaction
- Tkinter for early testing (simple local UI).
- Vue.js/React for final web-based interface (interactive bin/rack visualization).
- Implement color-coded indicators for kit statuses.
- Functionality
- Check-in/out system for parts.
- Kit tracking (assigned tech, due date, work order).
- Status updates (completed, pending, in progress).
- Search & filter for quick lookups.
- Standalone Hosting
- Local SQLite for early testing, then migrate to Oracle SQL.
- Flask/FastAPI for backend API handling.
- Serve locally via a simple Python-based web server.
- Future Enhancements
- Barcode scanning for quick kit identification or data entry iinto Kit details like adding parts to a kit instead of typing them out (becaue we wont be tied into the parts system unless i ever get approval from corporate but i could get a non updating copy of the parts and just scrub QTY and stuff and use it as a way to select parts it just wont be tied into anything)
- Automated alerts for overdue kits.
- Drag-and-drop UI for rack/bin visualization.
