from users.decorators import role_required

@role_required(['ADMIN'])
def admin_view(request):
    # Only admins can access this view
    pass
