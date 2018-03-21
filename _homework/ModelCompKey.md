##HW Key


| Model | Score | LR |
|-------|-------|----|
| Jukes-Cantor | -6424.20245 |    |
| F81   | -6303.66088  | 2\*(-6424.20245- -6303.66088) = 241.08314|  
| K80   | -6144.53846  | 2\*(-6424.20245- -6144.53846) = -559.32798 | 

How will we procede? Which model wins? What does this mean for which models we test next? 

What will be our PAUP specifications for the set of models we will test? Let's work them out as a group:


| Model | nst | basefr | Invariant sites? | Gamma Distributed rate heterogeneity | Score | LR |
|-------|-------|----|------|-------| -------|-----|
| SYM | nst= 6   |  basefr= eq | no | gamma = no| L= 5989.38158 | 2\*(-6144.53846--5989.38158) = 310.31376 | 
| SYM+I   | nst= 6  | basefr= eq| yes | gamma = no | L= -5982.71346 | 2\*(-5989.38158--5982.71346) = |
| SYM + I + G   | nst= 6 | basefr= eq | yes | yes | L= | 2\*(-5982.71346-5971.83486) = |


| Model | Score | AIC | Delta AIC |
|-------|-------|----|------------|
| Jukes-Cantor | -6424.20245 |  -12848.4049 = -2 ( ln ( -6424.20245 )) + 2 K   | |
| F81   | -6303.66088  | 12609.32176 = -2 (-6303.66088 ) + 2 \*1  | -12609.32176 - -12848.4049 = 239|
| K80   | -6144.53846  | 12291.07692 = -2(-6144.53846) + 2 \*1 | 12291.07692 - 12609.32176 = 318 |