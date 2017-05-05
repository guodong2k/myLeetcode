-- 175. Combine Two Tables   
select p.FirstName,p.LastName,a.City,a.State
from Person p
left join Address a on (p.PersonId=a.PersonId)

-- 176. Second Highest Salary
select max(Salary) as SecondHighestSalary from Employee a where
Salary not in (select max(Salary) from Employee)

-- 177. Nth Highest Salary
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE i INT;
  SET i=N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT i, 1
  );
END

-- 178. Rank Scores   
SELECT Score,Rank
FROM (
SELECT Score,@curRank:=@curRank+ IF(@prevNum=Score,0,1) AS Rank,@prevNum:=Score
FROM Score s,
(SELECT @curRank:=0)a,
(SELECT @prevNum:= NULL)p
ORDER BY Score DESC)t

-- 180. Consecutive Numbers
select distinct a.Num as ConsecutiveNums
from logs a
join logs b on (a.id=b.id+1 and a.Num=b.Num)
join logs c on (a.id=c.id-1 and a.Num=c.Num)

-- 181. Employees Earning More Than Their Managers
select a.Name as Employee
from Employee a
join Employee b on (a.ManagerId = b.id)
where a.Salary>b.Salary


-- 182. Duplicate Emails
select Email from (select Email,count(1) counts from Person group by Email) as a where counts>1

-- 183. Customers Who Never Order
select name as Customers 
from Customers a
where not exists (select * from Orders b where a.id=b.CustomerId)

-- 184. Department Highest Salary
select c.name as Department,b.name as Employee,b.Salary
from
(select Departmentid,name Employee ,max(Salary) as Salary
from  Employee 
group by Departmentid) a
join Employee b on (a.Departmentid=b.Departmentid and a.Salary=b.Salary)
join Department c on (a.Departmentid=c.id)


select t.name as Department,s.Employee,s.Salary
from
(select a.Departmentid,a.name Employee,a.Salary,@rank:=(@rank+1)*if(@dpt=a.Departmentid,1,0) as rank,@dpt:=a.Departmentid
from  Employee a,
(select @rank:=0) b,
(select @dpt:=NULL) c
order by a.Departmentid,a.Salary desc) s
join Department t on (s.Departmentid=t.id)
where s.rank<3

-- 185. Department Top Three Salaries
select t.name as Department,r.name as Employee,r.Salary
from
    (select distinct Salary,Departmentid
    from 
        (select a.Departmentid,a.Salary,@rank:=(@rank+if(@emp=a.Salary,0,1))*if(@dpt=a.Departmentid,1,0) as rank,@dpt:=a.Departmentid,@emp:=a.Salary
        from  Employee a,
        (select @rank:=0) b,
        (select @dpt:=NULL) c,
        (select @emp:=NULL) d
        order by a.Departmentid,a.Salary desc) n where n.rank<3) s
    join Employee r on (r.Salary=s.Salary and r.Departmentid=s.Departmentid)
    join Department t on (s.Departmentid=t.id)
order by t.name,r.Salary

-- 196. Delete Duplicate Emails
DELETE a  
FROM Person a ,Person b  
WHERE a.Email=b.Email 
and a.Id>b.Id; 

-- 197. Rising Temperature
select a.id as Id
  from Weather a
  join Weather b on a.date=date_add(b.date, interval 1 day)
 where a.Temperature>b.Temperature
 
-- 262. Trips and Users
select a.Request_at as Day,
       cast(format(sum(case when a.Status!='completed' then 1 else 0 end)/count(a.id),2) as DECIMAL(1,2)) as "Cancellation Rate"
from Trips a
join (select * from Users where role='client' and Banned='NO') b on (a.Client_Id=b.Users_Id)
join (select * from Users where role='driver' and Banned='NO') c on (a.Driver_Id=c.Users_Id)
where a.Request_at>='2013-10-01' and a.Request_at<='2013-10-03'
group by a.Request_at
 
 