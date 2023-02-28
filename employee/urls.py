from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
     path('',views.emp_employee_login,name='employee_login'),
     path('employee_logout',views.emp_employee_logout,name='employee_logout'),
     path('dashboard',views.emp_dashboard,name='emp_dashboard'),
     path('total_booking',views.emp_total_booking,name='emp_tbooking'),
     path('completed_booking',views.emp_completed_booking,name='emp_cbooking'),
     path('pending_booking',views.emp_pending_booking,name='emp_pbooking'),
     path('employee_register',views.emp_employee_register,name='emp_employee_register'),
     path('employee_management',views.emp_employee_management,name='emp_employee_management'),
     path('Service History',views.emp_service_history,name='emp_serviceHistory'),
     path('feedbacks',views.emp_feedbacks,name='emp_feedbacks'),
     path('messages',views.emp_messages,name='emp_messages'),
     path('customers',views.emp_customers,name='emp_customers'),
     path('change_password',views.emp_change_password,name='emp_change_password'),
     path('emp_profile',views.emp_profile,name='emp_profile'),
     path('edit_data',views.editData,name='edit_data'),
     path('delete_message/<int:id>',views.emp_delete_message,name='delete_message'),
     path('delete_feedback/<int:id>',views.emp_delete_feedback,name='delete_message'),
     path('delete_booking',views.deleteData,name='delete_booking'),
     path('cancel_booking/<int:id>',views.cancel_booking,name='cancel_booking'),

]