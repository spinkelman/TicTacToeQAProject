def edit_eda_settings_checkbox(self, checkbox_label, checkbox_toggle):
        """ Updates the checkbox_label value to checkbox_toggle in the EDA settings page """
        locator_checkbox_default = eda_lex_locators["eda_settings"]["checkbox_default"].format(checkbox_label)
        locator_checkbox = eda_lex_locators["eda_settings"]["checkbox"].format(checkbox_label)
        locator_edit = eda_lex_locators["eda_settings"]["edit"]
        locator_save = eda_lex_locators["eda_settings"]["save"]

        checkbox_default = self.selenium.get_element_attribute(locator_checkbox_default, "alt")
        if checkbox_default == checkbox_toggle:
            return
        else:
            self.selenium.click_element(locator_edit)
            self.selenium.wait_until_page_contains_element(
                locator_checkbox,
                error="Checkbox not found on the page"
            )
            self.selenium.click_element(locator_checkbox)
            self.selenium.click_element(locator_save)
            locator_toast = eda_lex_locators["success_message"].format("Settings successfully saved.")
            self.selenium.wait_until_page_contains_element(locator_toast)
