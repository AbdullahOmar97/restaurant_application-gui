import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantMenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Menu")

        # Pizza Section
        self.pizza_quantity_label = tk.Label(root, text="Pizza Quantity")
        self.pizza_quantity_label.grid(row=0, column=0)
        self.pizza_quantity = tk.Entry(root)
        self.pizza_quantity.grid(row=0, column=1)

        self.pizza_size_label = tk.Label(root, text="Pizza Size")
        self.pizza_size_label.grid(row=0, column=2)
        self.pizza_size = ttk.Combobox(root, values=["Small", "Medium", "Large"])
        self.pizza_size.grid(row=0, column=3)

        # Burger Section
        self.burger_quantity_label = tk.Label(root, text="Burger Quantity")
        self.burger_quantity_label.grid(row=1, column=0)
        self.burger_quantity = tk.Entry(root)
        self.burger_quantity.grid(row=1, column=1)

        self.burger_size_label = tk.Label(root, text="Burger Size")
        self.burger_size_label.grid(row=1, column=2)
        self.burger_size = ttk.Combobox(root, values=["Classic", "Big"])
        self.burger_size.grid(row=1, column=3)

        # Soft Drink Section
        self.soft_drink_quantity_label = tk.Label(root, text="Soft Drink Quantity")
        self.soft_drink_quantity_label.grid(row=2, column=0)
        self.soft_drink_quantity = tk.Entry(root)
        self.soft_drink_quantity.grid(row=2, column=1)

        # Order Type
        self.order_type_label = tk.Label(root, text="Order Type")
        self.order_type_label.grid(row=3, column=0)
        self.order_type = tk.StringVar(value="Takeaway")
        self.takeaway_radiobutton = tk.Radiobutton(root, text="Takeaway", variable=self.order_type, value="Takeaway")
        self.dinein_radiobutton = tk.Radiobutton(root, text="Dine in", variable=self.order_type, value="Dine in")
        self.takeaway_radiobutton.grid(row=3, column=1)
        self.dinein_radiobutton.grid(row=3, column=2)

        # Extras
        self.extra_cheese = tk.BooleanVar()
        self.extra_ketchup = tk.BooleanVar()
        self.extra_cheese_checkbox = tk.Checkbutton(root, text="Extra Cheese", variable=self.extra_cheese)
        self.extra_ketchup_checkbox = tk.Checkbutton(root, text="Extra Ketchup", variable=self.extra_ketchup)
        self.extra_cheese_checkbox.grid(row=4, column=0)
        self.extra_ketchup_checkbox.grid(row=4, column=1)

        # Order Summary Button
        self.order_summary_button = tk.Button(root, text="Order Summary", command=self.show_order_summary)
        self.order_summary_button.grid(row=5, column=0, columnspan=4)

    def show_order_summary(self):
        pizza_qty = int(self.pizza_quantity.get() or 0)
        pizza_size = self.pizza_size.get()
        burger_qty = int(self.burger_quantity.get() or 0)
        burger_size = self.burger_size.get()
        soft_drink_qty = int(self.soft_drink_quantity.get() or 0)
        order_type = self.order_type.get()
        extra_cheese = self.extra_cheese.get()
        extra_ketchup = self.extra_ketchup.get()

        total_price = (pizza_qty * {"Small": 5, "Medium": 7, "Large": 10}.get(pizza_size, 0) +
                       burger_qty * {"Classic": 5, "Big": 7}.get(burger_size, 0) +
                       soft_drink_qty * 2 +
                       extra_cheese * 1 +
                       extra_ketchup * 1)

        summary = (f"Order Type: {order_type}\n"
                   f"Pizza: {pizza_qty} x {pizza_size}\n"
                   f"Burger: {burger_qty} x {burger_size}\n"
                   f"Soft Drink: {soft_drink_qty}\n"
                   f"Extra Cheese: {'Yes' if extra_cheese else 'No'}\n"
                   f"Extra Ketchup: {'Yes' if extra_ketchup else 'No'}\n"
                   f"Total Price: JD {total_price}")

        messagebox.showinfo("Order Summary", summary)

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantMenuApp(root)
    root.mainloop()
