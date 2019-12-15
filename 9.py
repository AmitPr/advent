import sys


class opc:
    def __init__(self, filename, inputs=[], returnOut=False):
        self.inst = [int(x) for x in open(filename).read().split(',')]
        self.inst.extend([0] * 20000)
        self.ptr = 0
        self.curArg = 0
        self.relativeBase = 0
        self.inputs = inputs
        self.returnOut = returnOut
        self.outputs = []

    def param(self, pos, mode):
        if mode == 1:
            # Immediate value
            return self.inst[pos]
        elif mode == 2:
            # Relative Value
            # print("check",pos+self.relativeBase)
            return self.inst[self.inst[pos] + self.relativeBase]
        else:
            # Positional value
            return self.inst[self.inst[pos]]

    def op_params(self, pos):
        # Pad with 0s for missing parameters
        code = str(self.inst[pos]).zfill(5)
        # Opcode is last two digits
        op = self.inst[self.ptr] % 100
        # reverses all the digits but the last two
        p = [int(x) for x in code[:-2]][::-1]
        return op, p

    def op(self):
        # Parameters per Opcode
        p_per_op = {1: 3, 2: 3, 3: 1, 4: 1,
                    5: 2, 6: 2, 7: 3, 8: 3, 9: 1, 99: 0}
        op, params = self.op_params(self.ptr)
        pOffset = [self.relativeBase if x == 2 else 0 for x in params]
        # Exit op code
        if op == 99:
            return -1
        # preload parameters
        p1 = self.param(self.ptr + 1, params[0])
        p2, p3 = 0, 0
        # Make sure opcode is implemented
        try:
            if p_per_op[op] > 1:
                p2 = self.param(self.ptr + 2, params[1])
                if p_per_op[op] > 2:
                    p3 = self.param(self.ptr + 3, params[2])
        except:
            print("Unknown Opcode Error:", op)
        #Add(1)/Multiply (2)
        if op == 1 or op == 2:
            self.inst[self.inst[self.ptr + 3] + pOffset[2]
                      ] = p1 + p2 if op == 1 else p1 * p2
            self.ptr += 4
        # Input(3)
        elif op == 3:
            x = 0
            if self.curArg < len(self.inputs):
                x = self.inputs[self.curArg]
                self.curArg += 1
            else:
                x = int(input('in: '))
            self.inst[self.inst[self.ptr + 1] + pOffset[0]] = x
            self.ptr += 2
        # Print(4)
        elif op == 4:
            if self.returnOut:
                self.outputs.append(p1)
            else:
                print(p1)
            self.ptr += 2
        # Jump-if-false(5)/Jump-if-true(6)
        elif op == 5 or op == 6:
            if (p1 == 0 and op == 6) or (p1 != 0 and op == 5):
                self.ptr = p2
            else:
                self.ptr += 3
        # Less than(7)/Equal to(8)
        elif op == 7 or op == 8:
            if (p1 < p2 and op == 7) or (p1 == p2 and op == 8):
                self.inst[self.inst[self.ptr + 3] + pOffset[2]] = 1
            else:
                self.inst[self.inst[self.ptr + 3] + pOffset[2]] = 0
            self.ptr += 4
        elif op == 9:
            self.relativeBase += p1
            self.ptr += 2
        return 0

    def run(self, curInput=[], resetOut=False):
        if resetOut:
            self.outputs = []
        self.inputs.extend(curInput)
        code = 0
        # Run until exit code reached
        while code != -1:
            code = self.op()
        return self.outputs


if __name__ == "__main__":
    computer = opc(sys.argv[1])
    computer.run()
