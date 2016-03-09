#judge in position of (linenumber,rownumber) is Helix or not
def position_h(linen,rown):
        strlist=open('strlist.txt','r').read().split('\n')
        if strlist[linen][rown] == 'H':
                return '+1'
        else:
                return '-1'
        strlist.close()

#the line number (below) is the row number above. the name of file (below) is the line number above.                
import math
n=0
strlist=open('strlist.txt','r').read().splitlines()
while (n<200):
        seq='sequence'+str(n)
        lines=open(seq+'.psi','r').readlines()[3:-6]
        w=open(seq+'.txt','w')
        ln=0
        for line in lines:
                rn=1
                w.write(position_h(n,ln)+' ')
                for i in line[9:69].split():
                        w.write('%d' %rn+':'+'%.4f' %(float(1/(1+math.exp(-float(i)))))+' ')
                        rn=rn+1
                ln=ln+1
                w.write('\n')      
        w.close()
        ln=0
        n=n+1
        
        
#build a dict {name:seqfileabove}
#then translate cdhit file by this dict
#done
