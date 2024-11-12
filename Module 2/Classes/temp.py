

class Temperature:
    def __init__(self):
        self._temperature = 0

    def temperatureCelcius(self, tmp):
        self.temperatureKelvin(tmp+273.15)
    
    def temperatureKelvin(self, tmp):
        if(tmp<0):
            print("La température  ne peut pas être moins que 0 K")
            return
        self._temperature = tmp

    
    def temperatureFarenheit(self, tmp):
        self.temperatureKelvin((tmp-32)*5/9+273.15)

    def getTempKelvin(self):
        return self._temperature

    def getTempFarenheit(self):
        return (self.getTempKelvin()-273.15)*9/5+32

    def getTempCelcius(self):
        return self.getTempKelvin()-273.15
    


temperature = Temperature()

temperature.temperatureFarenheit(32)
print(temperature.getTempCelcius())
print(temperature.getTempFarenheit())
print(temperature.getTempKelvin())