% MATLAB code to read data, correct C_D values, and plot smooth C_D vs Alpha and C_L vs Alpha

% Define the full paths to each file in the Downloads folder
file_paths = {
    'C:\Users\youss\Downloads\airfoil_alpha_5_results.xlsx', ...
    'C:\Users\youss\Downloads\airfoil_alpha_10_results.xlsx', ...
    'C:\Users\youss\Downloads\airfoil_alpha_15_results.xlsx', ...
    'C:\Users\youss\Downloads\airfoil_alpha_20_results.xlsx'};

% Initialize arrays for storing data
data_all = cell(1, length(file_paths));
alpha_angles = [5, 10, 15, 20];  % Angles of attack in degrees

% Load, correct C_D, and store data
for i = 1:length(file_paths)
    % Read the table with preserved variable names
    data = readtable(file_paths{i}, 'VariableNamingRule', 'preserve');
    
    % Correct C_D column to be positive
    data.C_D = abs(data.C_D);
    
    % Save the modified data back to the file
    writetable(data, file_paths{i});
    
    % Store the corrected data
    data_all{i} = data;
end

% Initialize arrays for plotting
Reynolds_numbers = unique(data_all{1}.Re);  % Assuming each file has the same set of Re
CD_data = zeros(length(Reynolds_numbers), length(alpha_angles));
CL_data = zeros(length(Reynolds_numbers), length(alpha_angles));

% Extract C_D and C_L values for each angle and Reynolds number
for i = 1:length(data_all)
    data = data_all{i};
    for j = 1:length(Reynolds_numbers)
        idx = find(data.Re == Reynolds_numbers(j));  % Find rows with the current Re
        if ~isempty(idx)
            CD_data(j, i) = data.C_D(idx);
            CL_data(j, i) = data.C_L(idx);
        end
    end
end

% Add (alpha = 0, C_L = 0) for all Reynolds numbers
alpha_angles_with_zero = [0, alpha_angles];
CD_data_with_zero = CD_data;  % Leave C_D unchanged
CL_data_with_zero = [zeros(length(Reynolds_numbers), 1), CL_data];  % Add zero at alpha = 0

% Define finer range for alpha for smooth plotting
alpha_fine = linspace(0, max(alpha_angles), 100);

% Plot smooth C_D vs Alpha for each Reynolds number using spline interpolation
figure;
hold on;
for j = 1:length(Reynolds_numbers)
    % Fit a spline to smooth out the data for C_D
    CD_smooth = spline(alpha_angles, CD_data(j, :), alpha_fine); % spline interpolation
    plot(alpha_fine, CD_smooth, '-', 'LineWidth', 1.5, 'DisplayName', sprintf('Re = %.0f', Reynolds_numbers(j)));
end
hold off;
xlabel('\alpha (degrees)');
ylabel('C_D');
title('C_D vs \alpha for Different Reynolds Numbers');
legend('show');
grid on;

% Plot smooth C_L vs Alpha for each Reynolds number using spline interpolation
figure;
hold on;
for j = 1:length(Reynolds_numbers)
    % Fit a spline to smooth out the data for C_L
    CL_smooth = spline(alpha_angles_with_zero, CL_data_with_zero(j, :), alpha_fine); % spline interpolation
    plot(alpha_fine, CL_smooth, '-', 'LineWidth', 1.5, 'DisplayName', sprintf('Re = %.0f', Reynolds_numbers(j)));
end
hold off;
xlabel('\alpha (degrees)');
ylabel('C_L');
title('C_L vs \alpha for Different Reynolds Numbers');
legend('show');
grid on;
