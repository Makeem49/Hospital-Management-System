# Hospital-Management-System
## The following are the functionality this web application  possess

Admin
    1. Signup their account. Then Login (No approval Required).
    2. Can register/view/approve/reject/delete doctor (approve those doctor who applied for job in their hospital).
    3. Can admit/view/approve/reject/discharge patient (discharge patient when treatment is done).
    4. Can Generate/Download Invoice pdf (Generate Invoice according to medicine cost, room charge, doctor charge and other charge).
    5. Can view/book/approve Appointment (approve those appointments which is requested by patient).

Doctor
    1. Apply for job in hospital. Then Login (Approval required by hospital admin, Then only doctor can login).
    2. Can only view their patient details (symptoms, name, mobile ) assigned to that doctor by admin.
    3. Can view their discharged(by admin) patient list.
    4. Can view their Appointments, booked by admin.
    5. Can delete their Appointment, when doctor attended their appointment.

Patient
    1. Create account for admit in hospital. Then Login (Approval required by hospital admin, Then only patient can login).
    2. Can view assigned doctor's details like ( specialization, mobile, address).
    3. Can view their booked appointment status (pending/confirmed by admin).
    4. Can book appointments.(approval required by admin)
    5. Can view/download Invoice pdf (Only when that patient is discharged by admin).