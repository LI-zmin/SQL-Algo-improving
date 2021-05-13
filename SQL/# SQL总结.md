# SQL总结
## 查询
### ex1
```sql
select who from nameOfTable where condition
```
ex: 
```sql
select name, gdp/population from world where area>500
```
### ex2 查询在列表中的特定的值
```sql
select name,population from world 
    where name in ('France', 'China', 'Cuba')
```
### 以某个字母开头，结尾

``` sql
select name from world 
    where name LIKE 'F%'
```
这里%起到的是代替的作用
