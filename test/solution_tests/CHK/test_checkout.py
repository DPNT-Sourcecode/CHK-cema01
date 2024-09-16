from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout("3A") == 130
        assert checkout_solution.checkout("3A1B") == 160
        assert checkout_solution.checkout("3A2B") == 175
        assert checkout_solution.checkout("B") == 30
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

        assert checkout_solution.checkout("HHHHH") == 45  # 5H for 45
        assert checkout_solution.checkout("HHHHHHHHHH") == 80  # 10H for 80
        assert checkout_solution.checkout("KK") == 150  # 2K for 150
        assert checkout_solution.checkout("NNNM") == 120  # 3N for 120, M is free
        assert checkout_solution.checkout("RRRQ") == 150  # 3R for 150, Q is free
        assert checkout_solution.checkout("UUUU") == 120  # 4U for 120 (3U + 1U free)
        assert checkout_solution.checkout("VVV") == 130  # 3V for 130
        assert checkout_solution.checkout("VV") == 90  # 2V for 90


        assert checkout_solution.checkout("STX") == 45  # Group discount applies
        assert checkout_solution.checkout("SSTTXX") == 90  # Two group discounts apply
        assert checkout_solution.checkout("STXY") == 62  # Group discount applies, plus one item at normal price
        assert checkout_solution.checkout("SSSTTT") == 90  # Two group discounts apply
        assert checkout_solution.checkout("XYZ") == 45  # Group discount applies
        assert checkout_solution.checkout("SX") == 37  # No group discount, prices are normal

        # New tests for added items
        assert checkout_solution.checkout("HHHHH") == 45  # 5H for 45
        assert checkout_solution.checkout("HHHHHHHHHH") == 80  # 10H for 80
        assert checkout_solution.checkout("KK") == 120  # 2K for 120
        assert checkout_solution.checkout("NNNM") == 120  # 3N for 120, M is free
        assert checkout_solution.checkout("RRRQ") == 150  # 3R for 150, Q is free
        assert checkout_solution.checkout("UUUU") == 120  # 4U for 120 (3U + 1U free)
        assert checkout_solution.checkout("VVV") == 130  # 3V for 130
        assert checkout_solution.checkout("VV") == 90  # 2V for 90





