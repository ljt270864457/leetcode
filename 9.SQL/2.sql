-- 查找入职员工时间排名倒数第三的员工所有信息，为了减轻入门难度，目前所有的数据里员工入职的日期都不是同一天
CREATE TABLE `employees` (
`emp_no` int(11) NOT NULL,
`birth_date` date NOT NULL,
`first_name` varchar(14) NOT NULL,
`last_name` varchar(16) NOT NULL,
`gender` char(1) NOT NULL,
`hire_date` date NOT NULL,
PRIMARY KEY (`emp_no`));

-- emp_no	birth_date	first_name	last_name	gender	hire_date

-- 10008   1958-02-19    Saniya      Kalloufi      M     1994-09-15

select
    *
from
    employees
order by
    hire_date desc
limit 2,1