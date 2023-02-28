from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
     path('',views.admin_login,name='admin_login'),
     path('admin_logout',views.admin_logout,name='admin_logout'),
     path('dashboard',views.dashboard,name='dashboard'),
     path('total_booking',views.total_booking,name='tbooking'),
     path('completed_booking',views.completed_booking,name='cbooking'),
     path('pending_booking',views.pending_booking,name='pbooking'),
     path('employee_register',views.employee_register,name='employee_register'),
     path('employee_management',views.employee_management,name='employee_management'),
     path('Service History',views.service_history,name='serviceHistory'),
     path('feedbacks',views.feedbacks,name='feedbacks'),
     path('messages',views.messages,name='messages'),
     path('customers',views.customers,name='customers'),
     path('edit_employee/<int:id>',views.edit_employee,name='edit_employee'),
     path('emp_email_check',views.emp_email_check,name='emp_email_check'),
     path('emp_number_check',views.emp_number_check,name='emp_number_check'),
     path('edit_employee_data',views.edit_employee_data,name='edit_employee_data'),
     path('delete_employee_data/<int:id>',views.delete_employee_data,name='delete_employee_data'),
     path('delete_message/<int:id>',views.delete_message,name='delete_message'),
     path('delete_feedback/<int:id>',views.delete_feedback,name='delete_message'),
     path('edit_data',views.editData,name='edit_data'),
     path('edit_cust_data',views.edit_cust_data,name='edit_cust_data'),
     path('delete_booking',views.deleteData,name='delete_booking'),
     path('cancel_booking/<int:id>',views.cancel_booking,name='cancel_booking'),
     path('email_check',views.checkEmail,name='email_check'),

]