import tkinter
from breezypythongui import EasyFrame

class DrinkApp(EasyFrame):
    def __init__(self):
        """sets up the "home page" for the application"""
        EasyFrame.__init__(self, title="Drinks To Go")
        self.total = 0.00
        self.addLabel(text = "It’s a good day for coffee please select ‘New Drink’ to begin your order!", row = 0, column = 0)
        self.newdrink = self.addButton(text="New Drink", row=2,
                                    column=0, columnspan = 1, command=self.newDrink)

    def newDrink(self):
        """Gives the user the choice on which type of drink they want to order"""
        EasyFrame.__init__(self, title = "Drinks To Go - Drink Selection")
        self.addLabel(text = "Drink Choices", row=0, column=0)
        self.drinkTypes = self.addRadiobuttonGroup(row=1, column=0, rowspan=4)
        defaultRB = self.drinkTypes.addRadiobutton(text = "Coffee")
        self.drinkTypes.setSelectedButton(defaultRB)
        self.drinkTypes.addRadiobutton(text = "Tea")
        self.drinkTypes.addRadiobutton(text = "Smoothie")
        self.size = self.addButton(text ="Choose Size", row=1, column = 1, columnspan = 1, command= self.chooseSize)

    def finishOrder(self):
        """Finishes off the order and returns the users total"""
        EasyFrame.__init__(self, title = "Drinks To Go - Finish Order")
        self.addLabel(text = "Thank you for using Drinks To Go, your total will be $" + str(self.total)
                             + " when you pick up your drink(s)", row=0, column=0)

    def chooseSize(self):
        """Gives the user the choices for their drink size"""
        self.size["state"]="disabled"
        self.addLabel(text="Size Selection", row=0, column=0)
        self.drinkSizes = self.addRadiobuttonGroup(row=1, column=0, rowspan=2)
        if (self.drinkTypes.getSelectedButton()["text"] == "Coffee"):
            defaultRB = self.drinkSizes.addRadiobutton(text="8 ounces      $2.00")
            self.drinkSizes.setSelectedButton(defaultRB)
            self.drinkSizes.addRadiobutton(text="16 ounces      $2.50")
            self.drinkSizes.addRadiobutton(text="24 ounces      $3.00")
            self.addButton(text="Customize", row=1, column=1, columnspan=1, command=self.coffeeCustomize)
        if (self.drinkTypes.getSelectedButton()["text"] == "Tea"):
            defaultRB = self.drinkSizes.addRadiobutton(text="8 ounces      $1.50")
            self.drinkSizes.setSelectedButton(defaultRB)
            self.drinkSizes.addRadiobutton(text="16 ounces      $2.00")
            self.drinkSizes.addRadiobutton(text="24 ounces      $2.50")
            self.addButton(text="Customize", row=1, column=1, columnspan=1, command=self.teaCustomize)
        if (self.drinkTypes.getSelectedButton()["text"] == "Smoothie"):
            defaultRB = self.drinkSizes.addRadiobutton(text="8 ounces      $2.50")
            self.drinkSizes.setSelectedButton(defaultRB)
            self.drinkSizes.addRadiobutton(text="16 ounces      $3.00")
            self.drinkSizes.addRadiobutton(text="24 ounces      $3.50")
            self.addButton(text="Customize", row=1, column=1, columnspan=1, command=self.smoothieCustomize)

    def coffeeCustomize(self):
        """if a user orders coffee the customizations pop up"""
        EasyFrame.__init__(self, title="Drinks To Go - Customization")
        self.customizations1 = self.addRadiobuttonGroup(row=0, column=0, rowspan=2)
        self.customizations2 = self.addRadiobuttonGroup(row=0, column=1, rowspan=4)
        self.customizations3 = self.addRadiobuttonGroup(row=0, column=2, rowspan=2)
        if(self.drinkSizes.getSelectedButton()["text"] == "8 ounces      $2.00"):
            self.total = self.total + 2.00
        if (self.drinkSizes.getSelectedButton()["text"] == "16 ounces      $2.50"):
            self.total = self.total + 2.50
        if (self.drinkSizes.getSelectedButton()["text"] == "24 ounces      $3.00"):
            self.total = self.total + 3.00
        defaultRB1 = self.customizations1.addRadiobutton(text="Hot")
        self.customizations1.setSelectedButton(defaultRB1)
        self.customizations1.addRadiobutton(text="Iced")
        defaultRB2 = self.customizations2.addRadiobutton(text="None")
        self.customizations2.setSelectedButton(defaultRB2)
        self.customizations2.addRadiobutton(text="French Vanilla")
        self.customizations2.addRadiobutton(text="Caramel")
        self.customizations2.addRadiobutton(text="Mocha")
        defaultRB3 = self.customizations3.addRadiobutton(text="None")
        self.customizations3.setSelectedButton(defaultRB3)
        self.customizations3.addRadiobutton(text="Whipped Cream")
        self.newdrink = self.addButton(text="New Drink", row=5,
                                       column=0, columnspan=1, command=self.newDrink)
        self.finish = self.addButton(text="Finish Order", row=5, column = 1, columnspan=1,command=self.finishOrder)

    def teaCustomize(self):
        """if a user orders tea the customizations pop up"""
        EasyFrame.__init__(self, title="Drinks To Go - Customization")
        self.customizations1 = self.addRadiobuttonGroup(row=1, column=0, rowspan=4)
        self.customizations1 = self.addRadiobuttonGroup(row=1, column=0, rowspan=4)
        self.customizations1 = self.addRadiobuttonGroup(row=1, column=0, rowspan=4)
        if (self.drinkSizes.getSelectedButton()["text"] == "8 ounces      $1.50"):
            self.total = self.total + 1.50
        if (self.drinkSizes.getSelectedButton()["text"] == "16 ounces      $2.00"):
            self.total = self.total + 2.00
        if (self.drinkSizes.getSelectedButton()["text"] == "24 ounces      $2.50"):
            self.total = self.total + 2.50
        defaultRB1 = self.customizations1.addRadiobutton(text="Hot")
        self.customizations1.setSelectedButton(defaultRB1)
        self.customizations1.addRadiobutton(text="Iced")
        defaultRB2 = self.customizations2.addRadiobutton(text="None")
        self.customizations2.setSelectedButton(defaultRB2)
        self.customizations2.addRadiobutton(text="Honey")
        self.customizations2.addRadiobutton(text="Sugar")
        defaultRB3 = self.customizations3.addRadiobutton(text="None")
        self.customizations2.setSelectedButton(defaultRB3)
        self.customizations2.addRadiobutton(text="Milk")
        self.newdrink = self.addButton(text="New Drink", row=2,
                                       column=0, columnspan=1, command=self.newDrink)
        self.finish = self.addButton(text="Finish Order", row=2, column=1, columnspan=1, command=self.finishOrder)

    def smoothieCustomize(self):
        """if a user orders smoothie the customizations pop up"""
        EasyFrame.__init__(self, title="Drinks To Go - Customization")
        self.customizations = self.addRadiobuttonGroup(row=1, column=0, rowspan=4)
        if (self.drinkSizes.getSelectedButton()["text"] == "8 ounces      $2.50"):
            self.total = self.total + 2.50
        if (self.drinkSizes.getSelectedButton()["text"] == "16 ounces      $3.00"):
            self.total = self.total + 3.00
        if (self.drinkSizes.getSelectedButton()["text"] == "24 ounces      $3.50"):
            self.total = self.total + 3.50
            """coffee, hot or iced, none french vanilla caramel or mocha, none or whipped cream
                            tea, hot or iced, none honey or sugar, none or milk
                            smoothie, strawberry banana blueberry spinich peaches cherry protien powder"""
            self.strCB= self.addCheckbutton(text="Strawberries", row =0, column =0)
            self.strCB = self.addCheckbutton(text="Bananas", row=0, column=1)
            self.strCB = self.addCheckbutton(text="Blueberries", row=0, column=2)
            self.strCB = self.addCheckbutton(text="Raspberries", row=0, column=3)
            self.strCB = self.addCheckbutton(text="Spinach", row=1, column=0)
            self.strCB = self.addCheckbutton(text="Peaches", row=1, column=1)
            self.strCB = self.addCheckbutton(text="Cherries", row=1, column=2)
            self.strCB = self.addCheckbutton(text="Protein Powder", row=1, column=3)
        self.newdrink = self.addButton(text="New Drink", row=2,
                                       column=0, columnspan=1, command=self.newDrink)
        self.finish = self.addButton(text="Finish Order", row=2, column=1, columnspan=1, command=self.finishOrder)

def main():
    DrinkApp().mainloop()


if __name__ == '__main__':
    main()
