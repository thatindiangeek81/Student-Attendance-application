def attendance(present, total):
    if total == 0:
        return 0
    return (present / total) * 100


def attendance_report(attendance_percentage):
    if attendance_percentage >= 75:
        return "Good"
    elif attendance_percentage >= 50:
        return "Average"
    else:
        return "Poor"