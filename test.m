elbow = load("right_elbow_coords.txt");
wrist = load("right_wrist_coords.txt");
%%
dist = zeros(1);
angle = zeros(1);
%%
for i = 1:10
    dist(i) = sqrt((wrist(1,1) - elbow(1,1))^2 + (wrist(1,2) - elbow(1,2))^2);
end
%%
for i = 1:10
    angle(i) = dist(i) / wrist(i,1);
end