import wx


class ShippingCalculator(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Shipping Calculator", size=(400, 300))
        self.panel = wx.Panel(self)

        # TextCtrl widgets for user input
        self.name_label = wx.StaticText(self.panel, label="Name:", pos=(20, 20))
        self.name_text = wx.TextCtrl(self.panel, pos=(90, 20), size=(220, -1))

        self.address_label = wx.StaticText(self.panel, label="Address:", pos=(20, 50))
        self.address_text = wx.TextCtrl(self.panel, pos=(90, 50), size=(220, -1))

        self.city_state_zip_label = wx.StaticText(self.panel, label="City, State, Zip:", pos=(20, 80))
        self.city_state_zip_text = wx.TextCtrl(self.panel, pos=(120, 80), size=(190, -1))

        # Radio buttons for package weight
        self.weight_label = wx.StaticText(self.panel, label="Package Weight (lbs):", pos=(20, 120))
        self.weight_1 = wx.RadioButton(self.panel, -1, '0 - 1.9', pos=(20, 140), style=wx.RB_GROUP)
        self.weight_2 = wx.RadioButton(self.panel, -1, '2 - 4.9', pos=(20, 160))
        self.weight_3 = wx.RadioButton(self.panel, -1, '5+', pos=(20, 180))

        # Radio buttons for shipping speed
        self.speed_label = wx.StaticText(self.panel, label="Shipping Speed:", pos=(150, 120))
        self.speed_1 = wx.RadioButton(self.panel, -1, 'Standard', pos=(150, 140), style=wx.RB_GROUP)
        self.speed_2 = wx.RadioButton(self.panel, -1, '2-Day', pos=(150, 160))
        self.speed_3 = wx.RadioButton(self.panel, -1, '3-Day', pos=(150, 180))
        self.speed_4 = wx.RadioButton(self.panel, -1, 'Next-Day', pos=(150, 200))

        # Check boxes for extras
        self.gift_wrap = wx.CheckBox(self.panel, -1, 'Gift Wrap ($5)', pos=(20, 220))
        self.insurance = wx.CheckBox(self.panel, -1, 'Insurance ($10)', pos=(20, 240))

        # Calculate and Clear buttons
        self.calculate_btn = wx.Button(self.panel, label="Calculate Total", pos=(250, 220))
        self.Bind(wx.EVT_BUTTON, self.calculate_total, self.calculate_btn)

        self.clear_btn = wx.Button(self.panel, label="Clear Form", pos=(250, 250))
        self.Bind(wx.EVT_BUTTON, self.clear_form, self.clear_btn)

        # Result label
        self.result_label = wx.StaticText(self.panel, label="", pos=(20, 270))

        self.Show()

    def calculate_total(self, event):
        # Placeholder function for calculating total
        total = 0
        # Dummy calculation for demonstration
        if self.gift_wrap.GetValue():
            total += 5
        if self.insurance.GetValue():
            total += 10
        self.result_label.SetLabel(f"Total Cost: ${total}")

    def clear_form(self, event):
        # Clear all input fields and reset result label
        self.name_text.Clear()
        self.address_text.Clear()
        self.city_state_zip_text.Clear()
        self.weight_1.SetValue(True)
        self.speed_1.SetValue(True)
        self.gift_wrap.SetValue(False)
        self.insurance.SetValue(False)
        self.result_label.SetLabel("")


if __name__ == "__main__":
    app = wx.App()
    frame = ShippingCalculator()
    app.MainLoop()
