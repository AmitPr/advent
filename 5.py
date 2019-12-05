import sys
class opc:
    def __init__(self, filename):
        self.inst = [int(x) for x in open(filename).read().split(',')]
        self.ptr = 0

    def param(self,pos,mode):
        if mode:
            #Immediate value
            return self.inst[pos]
        else:
            #Positional value
            return self.inst[self.inst[pos]]

    def op_params(self,pos):
        #Pad with 0s for missing parameters
        code = str(self.inst[pos]).zfill(5)
        #Opcode is last two digits
        op=self.inst[self.ptr]%100
        #reverses all the digits but the last two
        p = [int(x) for x in code[:-2]][::-1]
        return op,p

    def op(self):
        #Parameters per Opcode
        p_per_op = {1:3,2:3,3:1,4:1,5:2,6:2,7:3,8:3,99:0}
        op,params = self.op_params(self.ptr)
        #Exit op code
        if op==99:
            return -1
        #preload parameters
        p1 = self.param(self.ptr+1,params[0])
        p2,p3=0,0
        #Make sure opcode is implemented
        try:
            if p_per_op[op]>1:
                p2 = self.param(self.ptr+2,params[1])
                if p_per_op[op]>2:
                    p3 = self.param(self.ptr+3,params[2])
        except:
            print("Unknown Opcode Error:",op)
        #Add(1)/Multiply (2)
        if op==1 or op ==2:
            self.inst[self.inst[self.ptr+3]]= p1 + p2 if op ==1 else p1 * p2
            self.ptr+=4
        #Input(3)
        elif op==3:
            self.inst[self.inst[self.ptr+1]]=int(input('Op[3]: '))
            self.ptr+=2
        #Print(4)
        elif op==4:
            print("Op[4]:",p1)
            self.ptr+=2
        #Jump-if-false(5)/Jump-if-true(6)
        elif op==5 or op==6:
            if (p1==0 and op==6) or (p1!=0 and op==5):
                self.ptr=p2
            else:
                self.ptr+=3
        #Less than(7)/Equal to(8)
        elif op==7 or op==8:
            if (p1 < p2 and op == 7) or (p1==p2 and op == 8):
                self.inst[self.inst[self.ptr+3]]=1
            else:
                self.inst[self.inst[self.ptr+3]]=0
            self.ptr+=4
        return 0

    def run(self):
        code = 0
        #Run until exit code reached
        while code!=-1:
            code = self.op()

if __name__=="__main__":
    computer = opc(sys.argv[1])
    computer.run()
