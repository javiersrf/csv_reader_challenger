from io import BytesIO
from django.test import TestCase
from .models import Operation, ProviderSell, RegisterSell
from .controller import upload_controller

class HomeControllerTestCase(TestCase):
    def setUp(self):
        Operation.objects.create(name="xfile.txt", quantity=1000000, total = 1)
        Operation.objects.create(name="yfile.txt", quantity=1, total = 1000)

    def test_get_registers(self):
        operations = Operation.objects.all()
        self.assertEqual(len(operations),2)


class UploadControllerTestCase(TestCase):
    def setUp(self):
        data_mock = """Comprador	Descrição	Preço Unitário	Quantidade	Endereço	Fornecedor
        João Silva	R$10 off R$20 of food	10.0	2	987 Fake St	Bob's Pizza
        Amy Pond	R$30 of awesome for R$10	10.0	5	456 Unreal Rd	Tom's Awesome Shop
        Marty McFly	R$20 Sneakers for R$5	5.0	1	123 Fake St	Sneaker Store Emporium
        Snake Plissken	R$20 Sneakers for R$5	5.0	4	123 Fake St	Sneaker Store Emporium            
        """
        data_mock = str.encode(data_mock)
        self.data = BytesIO(data_mock)
    def test_get_registers(self):
        self.data.seek(0)
        response = upload_controller.normalize_data(self.data)
        assert response["total"] >0
        assert response["quantity"] >0
        assert len(response["providers"]) > 0
        assert len(response["registers"]) > 0