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

        assert checkout_solution.checkout("EEBB") == 110
        assert checkout_solution.checkout("EEB") == 80
        assert checkout_solution.checkout("EE") == 80
        assert checkout_solution.checkout("AAAAABEEB") == 295
        assert checkout_solution.checkout("3A2BEE") == 255  # 3A for 130, 2B for 45, 2E for 80 (B is free)



