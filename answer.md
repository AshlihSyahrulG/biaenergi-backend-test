# Question #1 (maintenance)
```py
def multiply(x, y):
    total = 0
    while x > 0:
        total += y
        x -= 1
    return total
```
QUESTIONS:

● What is wrong with the above code?

Sebenarnya dari kode di atas itu tidak ada yang salah , akan tetapi saya melakukan refactor terhadap kode tersebut sehingga jika dikali dengan angka mines maka ia akan mengeluarkan output 0

● If you find it wrong, please fix the code above without using the “*” or “/” operator or Absolute call? 

● As part of our development process we test all methods at a code level. Which input values would you use to do the testing? 

saya melakukan pengujian di angka positif dan negatif lalu 0 saya coba untuk melakukan testing

● For later discussion: What else worries you as you fix this problem?

Semuanya berjalan dengan baik dan tidak ada yang perlu saya hawatirkan


# Question #2 (SQL)

```
Select USA.NAME, EU.NAME From USA, EU Where USA.ID = EU.ID
[[Thomas],[Thomas]]
```

```
Select USA.NAME, EU.NAME From USA left join EU on (USA.ID = EU.ID)
[[Thomas, Cindy],[Thomas, null]]
```

```
Select USA.NAME, EU.NAME From USA, EU
[[Thomas, Cindy],[Thomas, Francois]]
```

we use those tables to keep track of our European and American customers. Please provide a critique to that table design (is it good? How could it be better?).

colom pada tabel terlalu sedikit, menurut saya akan jauh lebih baik apabila colomnya ditambahkan dengan colom yang lebih banyak seperti email , nomer tlp, dll

# Question #3 (algorithm)

QUESTION:

Write the content of the method below that counts the maximum number of levels in a given tree. Please notice that this is NOT counting the TOTAL number of nodes, but counting the DEPTH

untuk nomer 3 jawaban nya ada di question3.py

# Question #4 (performance)
QUESTIONS:

What would be the effect on performance in these two cases:
```
|        | bagA                         | bagB                        |
| -------| :---------------------------:| --------------------------: |
| Case 1 | Has LARGE number of elements |Has SMALL number of elements |
| Case 2 | Has SMALL number of elements |Has LARGE number of elements |

```

Do you have any recommendations to improve the performance? Feel free to change the above method.

answer : dengan meningkatkan versi menggunakan set python akan memiliki kompleksitas waktu yang umumnya kan lebih cepat dari pada versi asli

# Question #5 (algorithm)
QUESTION:

Please write a method to print out ALL the Prime numbers between 2 and 100.

untuk nomer 5 jawaban nya ada di question5.py