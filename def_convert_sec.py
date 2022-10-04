def convert_sec(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours*3600)//60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
a = convert_sec(1500) 
print(a)