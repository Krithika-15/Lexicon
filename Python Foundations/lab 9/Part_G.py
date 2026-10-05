class CPU:
    def __init__(self, model):
        self.model = model


class Computer:
    def __init__(self, brand, cpu):
        self.brand = brand
        self.cpu = cpu


cpu_1 = CPU("Intel Core i7-13700H")
computer_1 = Computer("Dell XPS 15", cpu_1)

print(f"Computer Brand : {computer_1.brand}\nCPU : {computer_1.cpu.model}")

# Here composition makes more sense because every computer has a CPU
# A CPU is a part inside Computer, so computer HAS-A CPU (Composition).
# Computer IS-A CPU is wrong, as it would mean a computer is a special kind of processor.
# Composition also lets us swap the CPU (pass a different CPU object) without changing the Computer class

print("""
Car/Engine => Car HAS-A Engine (Composition)
Manager/Employee => Manager IS-A Employee (Inheritance)
Course/Teacher => Course HAS-A Teacher (Composition)
Phone/Device => Phone IS-A Device (Inheritance)
""")

