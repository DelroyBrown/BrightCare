# BrightCare

BrightCare is a Django-based application designed for child care homes in the UK. The focus is to help staff manage records, conduct risk assessments, and track incidents for young persons in their care.

## Purpose

- Keep an organized record of each young person’s details
- Let staff create risk assessments and record incidents
- Control who can see or edit specific data based on care home assignments

## Features

1. **Staff Registration**  
   - Staff create accounts through a signup process.  
   - Admins or managers can approve and assign staff to one or more care homes.

2. **Young Persons Module**  
   - Stores basic info (name, date of birth, medical needs, etc.).  
   - Connects each young person to a care home and their guardians.

3. **Risk Assessments**  
   - Staff can add or update assessments for each young person.  
   - Includes fields for likelihood, impact, and overall level.

4. **Incidents**  
   - Logs any events that occur, who reported it, and the location.  
   - Links incidents to the relevant young person and staff member.

5. **Care Homes**  
   - Keeps details such as name, address, capacity, and registration number.  
   - Defines a manager (optional) and which staff are linked to that home.