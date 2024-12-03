# # Develop a test for add modification to test if Y input works and runs if a user puts Y
# # failed due to name error add_modifier not defined so will define add modifier:
# def add_modifier():
#     # need to add bare minimum code to pass the test
#     add_modifier = input("do you wish to add modifier? Y/N")
#     if add_modifier.upper() == "Y":
#         return "Y"
#     elif add_modifier.upper() == "N":
#         return "N"


# def test_input(monkeypatch):
#     monkeypatch.setattr("builtins.input", lambda _: "Y")
#     i = add_modifier()
#     assert i == "Y"


# def test_2(monkeypatch):
#     monkeypatch.setattr("builtins.input", lambda _: "N")
#     i = add_modifier()
#     assert i == "N"
