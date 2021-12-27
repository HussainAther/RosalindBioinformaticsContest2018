% Advent of Code Day 25
input = "./input-25-0.txt";
data = char(readlines(input));

map = data(1:end-1,:);
n = size(map,1);
i = 0;
while true
  i = i + 1;
  next = map;
  
  next(:,end+1) = next(:,1);
  ind = find(next == '>');
  next(:,end+1) = next(:,2);
  ind_ok = next(ind + n) == '.';
  
  next(ind(ind_ok) + n) = '>';
  next(ind(ind_ok)) = '.';
  next(:,1) = next(:,end-1);
  next(:,end-1:end) = [];
  
  next(end+1,:) = next(1,:);
  [r,c] = find(next == 'v');
  next(end+1,:) = next(2,:);
  ind = sub2ind(size(next), r, c);
  ind_ok = next(ind + 1) == '.';
  
  next(ind(ind_ok)+1) = 'v';
  next(ind(ind_ok)) = '.';
  next(1,:) = next(end-1,:);
  next(end-1:end,:) = [];
  
  if isequal(next, map)
    ans_1 = i
    break
  end
  map = next;
end

