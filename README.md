# Python implementation of Turing machines

### Turing complete languages

* A language is *Turing complete* if you can simulate a Turing machine with it.
* Thus Python is Turing complete.

### Calling the function

```python
table_reverse_binary = {
    ('s',' '):(' ','L','h'),
    ('s','0'):('1','R','s'),
    ('s','1'):('0','R','s')
}

tm = TuringMachine(table_reverse_binary, "110")

tm.run(show=True)
```

Outputs:

```
1, s1,  0,  
0,  1, s0,  
0,  0,  0, s
0,  0,  1,   , s
0,  0,  1, h ,  

'001'
```