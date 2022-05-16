from ..models import Operation

    
def get_registers():
    operations = Operation.objects.all()
    return operations