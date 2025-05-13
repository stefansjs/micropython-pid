class PID:
    def __init__(self, p=1, i=0, d=0.5):
        if abs(i) >= 1:
            raise ValueError("abs(i) > 1; the magnitude of the integral component cant be greater than 1")
        if abs(i) >= 0.95:
            print("This PID filter has a lot of ringing. It may behave poorly")

        self.b = [p, d]
        self.a = 0
        self.delay = 0

    def __call__(self, input):
        output = self.b[0] * input + self.b[1] * self.delay - self.a * self.delay
        self.delay = output
        return output
