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
        assert checkout_solution.checkout("AAAAABEEB") == 310  # 5A for 200, B for 30, 2E for 80 (B is free)
        assert checkout_solution.checkout("3ABEE") == 210  # 3A for 130, 1B for 45, 2E for 80 (B is free)
        assert checkout_solution.checkout("3A3BEE") == 255  # 3A for 130, 2B for 45, 2E for 80 (B is free)

        assert checkout_solution.checkout("F") == 10
        assert checkout_solution.checkout("FF") == 20
        assert checkout_solution.checkout("FFF") == 20 # 3F for 20
        assert checkout_solution.checkout("FFFF") == 30
        assert checkout_solution.checkout("FFFFFF") == 40 # 6F for 40







