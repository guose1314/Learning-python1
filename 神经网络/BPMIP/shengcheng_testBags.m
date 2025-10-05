function [testBags] = shengcheng_testBags(bagInf, instanceInf)
%本函数用于生成 测试用包 的CELL数组， 默认处理的数据集为MUSK1，取 前10个正包 和 前10个反包 共20个包作为测试用包
%要生成MUSK2的 测试用包，可改参数。
%2012/09/04    芮辰

bag_pointer=0;  %包指针
ins_pointer=1;    %示例指针

num_pos=47;            %正包数
num_pos_ins=207;
num_pos_test=10;     %正测试包数

testBags= {};        %初始化测试用包
 
for i = 1 : num_pos_test                                 %从第1个到第10个测试包
    bag_pointer = bag_pointer + 1;
    
    for j = 1 : instanceInf(i)
        testBags{bag_pointer, 1} (j, :)= bagInf(ins_pointer, :);       %生成前10个测试正包的 cell array
        ins_pointer= ins_pointer + 1;
    end  
end

ins_pointer=207;
ins_pointer = ins_pointer + num_pos_ins ;

for i = (num_pos +1) : (num_pos +10)
    bag_pointer = bag_pointer + 1;
    
    for j = 1 : instanceInf(i)
        testBags{bag_pointer, 1} (j, :)= bagInf(ins_pointer, :);    %生成反包的 cell array
        ins_pointer= ins_pointer + 1;
    end
    
end