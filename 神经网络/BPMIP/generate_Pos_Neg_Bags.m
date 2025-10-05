function [NCover, PCover] = generate_Pos_Neg_Bags (cpdp, numcp, fgs, ncovers, bagInf, train_instance)

[row,col] = size(train_instance);
coverInf = [];

for i = 1 : row
    coverInf(i, :) = bagInf(cpdp(1,i), :);
end

% cover_pointer=0;  %覆盖指针
% num_neg = ncovers(1, 1);                                     %反覆盖数
% num_pos = fgs - ncovers(1, 1);                             %正覆盖数

all_cover=fgs;
num_neg_cover = ncovers(1,1);                                           %反覆盖数
% num_pos_cover = all_cover - num_neg_cover;

NCover= {};        %初始化

neg_ins_pointer = 1;
neg_cover_pointer = 0;

for i = 1 : num_neg_cover
    neg_cover_pointer = neg_cover_pointer + 1;  
    for j = 1 : numcp(1, i)
        NCover{neg_cover_pointer, 1} (j, :) = coverInf(neg_ins_pointer, :);    %生成反包的 cell array
        neg_ins_pointer= neg_ins_pointer + 1;
    end
end

PCover={};

pos_ins_pointer = sum( numcp(1, 1 : num_neg_cover) );
pos_cover_pointer = 0;

for i = (num_neg_cover + 1) : all_cover
    pos_cover_pointer = pos_cover_pointer + 1;    
    for j = 1 : numcp(1, i)
        PCover{pos_cover_pointer, 1} (j, :) = coverInf(pos_ins_pointer, :);    %生成反包的 cell array
        pos_ins_pointer = pos_ins_pointer + 1;
    end  
end
