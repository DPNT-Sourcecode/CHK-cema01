from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout("3A") == 130
        assert checkout_solution.checkout("3A1B") == 160
        assert checkout_solution.checkout("3A2B") == 175
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("3A1X") == -1
        assert checkout_solution.checkout("3AX") == -1
        assert checkout_solution.checkout("a") == -1
        assert checkout_solution.checkout("-") == -1


