library(dplyr)
library(rafalib)
library(tidyverse)

irradiance <- read.csv("solar_radiation.csv")
cloud <- read.csv("cloud_cover.csv")
wind <- read.csv("wind_speed.csv")
irradiance <- na.omit(data)

data <- data.frame(irradiance, cloud, wind)

control <- filter(data, cloud > 1073 & wind < 7.87) %>% select(irradiance) %>% unlist
mean <- mean(control)
sd <- sd(control)

set.seed(1)

generate <- function(N,mean,sd){
  sample1 <- rnorm(N,mean,sd)
  sqrt(5)*mean(sample1)/sd(sample1)
  
}

samples <- generate(250, mean, sd)

val <- replicate(100000, {
  y <- d + rnorm(n,sd=1)
  X = cbind(1,tt,tt^2)
  A = solve(crossprod(X))%*%t(X)
  -2*(A%*%y)[3]
})

regres <- sqrt(mean((val-mean(val))^2))
