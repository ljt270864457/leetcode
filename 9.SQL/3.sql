-- 题目描述
-- 查找各个部门当前(dept_manager.to_date='9999-01-01')领导当前(salaries.to_date='9999-01-01')薪水详情以及其对应部门编号dept_no
-- (注:请以salaries表为主表进行查询，输出结果以salaries.emp_no升序排序，并且请注意输出结果里面dept_no列是最后一列)

CREATE TABLE `salaries` (
`emp_no` int(11) NOT NULL, -- '员工编号',
`salary` int(11) NOT NULL,
`from_date` date NOT NULL,
`to_date` date NOT NULL,
PRIMARY KEY (`emp_no`,`from_date`));

CREATE TABLE `dept_manager` (
`dept_no` char(4) NOT NULL, -- '部门编号'
`emp_no` int(11) NOT NULL, --  '员工编号'
`to_date` date NOT NULL,
PRIMARY KEY (`emp_no`,`dept_no`));

select
    t1.emp_no,
    t1.salary,
    t1.from_date,
    t2.to_date,
    t2.dept_no
from
    salaries t1
join
    dept_manager t2
on
    t1.emp_no = t2.emp_no
where
    t1.to_date='9999-01-01'
    and t2.to_date='9999-01-01'
order by
    t1.emp_no
