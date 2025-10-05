function y=min_max_norm(min_value,max_value,x)
%normalizing each column vector of matrix 'x' using min_max normalization
%min_value is the minimal value of the normalized region, where max_value is the corresponding maximal value of the normalized region

if(max_value<=min_value)
  error('max value can"t be lower than min value');
end

size_x=size(x);
y=zeros(size_x);
for col=1:size_x(2)
   max_col=max(x(:,col));
   min_col=min(x(:,col));
   for line=1:size_x(1)
      if(max_col==min_col)
         y(line,col)=(max_value+min_value)/2;
      else
         y(line,col)=((x(line,col)-min_col)/(max_col-min_col))*(max_value-min_value)+min_value;
      end
   end
end
