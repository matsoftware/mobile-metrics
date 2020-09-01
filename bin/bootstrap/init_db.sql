-- Create a new database called 'mobile_metrics'
-- Connect to the 'master' database to run this snippet
USE master
GO
-- Create the new database if it does not exist already
IF NOT EXISTS (
    SELECT [name]
        FROM sys.databases
        WHERE [name] = N'mobile_metrics
    '
)
CREATE DATABASE mobile_metrics
GO
-- Create a new table called '[TableName]' in schema '[dbo]'
CREATE TABLE IPASize
(
    ID INT NOT NULL PRIMARY KEY, -- Primary Key column
    app_name NVARCHAR(50) NOT NULL,
    report_time ROWVERSION NOT NULL,
    app_size NUMERIC NOT NULL,
    -- Specify more columns here
);
GO