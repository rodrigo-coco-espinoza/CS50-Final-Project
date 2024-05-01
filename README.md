# PC ISLA ADMINISTRATOR
### Name:Rodrigo Espinoza Fuentes
### Video demo: https://www.youtube.com/watch?v=TBujYFIlMK8
### App repository: https://github.com/rodrigo-coco-espinoza/CS50-Final-Project.git

## Project description
PC Isla Administrator is a web application for managing various projects within the tax administration area where I work. In my job, we provide access to 3 computers, called PC Isla, to other state institutions for project development and obtaining relevant information for their activities. Due to the sensitivity of the data we handle, institutions can only access aggregated statistical information, and the results of their research must undergo a rigorous analysis process. These computers allow access to our databases but do not have internet access or USB ports to extract information, hence their name "isla" (island).

For an institution to use these computers, they must go through the following stages:
1. The institution sends a formal request detailing the project's name, objective, and other details.
2. The tax administration approves or rejects the project.
3. If the project is approved, a "Usage Protocol" is drafted, a document that establishes the rules for computer use, specifies the head researcher and associated researchers, and assigns specific days and time slots (AM or PM) for use.
4. The institution develops its project for a maximum period of 3 months. During this time, attendance must be recorded each time researchers use the computer, which allows for evaluation of future projects with the institution (an institution that underuses the allocated time will be less considered in the future).

Up to this point, all this management has been done using Excel spreadsheets and physical paper for attendance tracking. This is why the PC Isla Administrator project aims to be a solution that facilitates, centralizes, and streamlines the management of these projects.

## About the App
This application was developed using Django, React, and Tailwind CSS. Although we learned Flask, Jinja, and Bootstrap in the course, I found it to be a good challenge to learn another stack and have more tools for the future.

One of the main reasons for choosing React was its ease of creating more responsive and interactive pages, enhancing navigation and user experience. Additionally, Django enables scalability of the application and provides useful tools such as the admin page to explore and edit the database.

**Backend**
The main folders and files in the backend are:

1. core/
Contains Django configuration files and backend URLs.
2. apps/
Here are the 2 backend applications:
- user: Contains user models and views for changing user passwords. User accounts can be of 3 types: admin (full access to the app), editor (tax administration official account, allows using the forms), researcher (allows recording attendance).
- pc_isla:  Contains models for tables needed for project management, such as Project (information for each project), Role (identifies a person as a researcher or head researcher of the project), Jornada (computer, day, and assigned time slot for the project), and Asistencia (attendance record of the project). It also contains all API endpoints for the application to function: registering a new project, recording response and usage protocol, marking attendance, etc.

3. media/proyectos_pc_isla/
This folder stores files uploaded by users to the application. For each project, a folder will be created containing all the files required for project management. File names are standardized before being saved.

**Frontend**
Except for the tailwind.config.js file, all frontend files developed are located in src/
The main folders and files in the frontend are:

1. tailwind.config.js
The specific color palette of the institution where I work has been added to give the application an official appearance.
2. styles/index.css
Most of the site's styling was done using Tailwind classes, but some changes were made with CSS, mainly to modify the scroll sidebar and create some animations.
3. redux/
Redux was used to manage the application's state variables. All API requests, whether on page load or when submitting a form, were made with Axios and defined through functions in actions/.
4. hocs/
Refers to Higher-order components and contains the website layout.
5. containers/pages/
Here are the three main pages of the application: Home, the PC Isla application, and the user page.
6. components/
Contains components for each page, allowing different parts to be worked on separately, simplifying files and maintaining development order. Additionally, components can be reused in different parts of the site.
- home/: Components for the home page of the app and each section it contains.
- pc_isla/: Components of the PC Isla application, divided into calendar components, active projects, forms, and modals.
- user/: Components for login, user page, and attendance registration.
- navigation/: Navbar and footer components.

**Enviroment files**
There are two .env files in the application, .env and core/.env, which contain information such as URLs, Django's secret key, and other parameters that are best kept hidden in a production environment. For this case, they have been included within the repository.

## Instructions
To run this app, you will need to create a new virtual environment and install all modules listed in requirements.txt for Python dependencies and all packages listed in package.json for Node.js dependencies.


The database was preloaded with example projects and user accounts. In this example, consider:

1. The tax administration is represented by HOGWARTS, with the following user accounts:
- Admin
albus.dumbledore (you can access the admin and view the database at http://127.0.0.1:8000/admin/)

- Editors 
minerva.mcgonagall
filius.flitwick
severus.snape
promona.sprout

2. Research institutions are represented by the four houses, each institution has a head researcher (represented by the house founder), who is assigned an account to mark attendance for their project(s). Other researchers (other house members) do not have user accounts.

GRYFFINDOR
godric.gryffindor

SLYTHERIN
salazar.slytherin

RAVENCLAW
rowena.ravenclaw

HUFFLEPUF
helga.hufflepuf

For each house, a project has been created to visualize the calendar and interact with the app. However, projects have a duration of 3 months, so after August 1, 2024, the projects will no longer appear on the calendar but will still appear as active projects since their status has not been changed. If you view the application after the specified date, I suggest accessing the database, changing the projects' status to 'Finalizado', and creating new projects following the example in the video.