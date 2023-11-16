library(tidyverse)
d <- read.delim("clipboard") # unique concepts

# create complete grid
new_grid <- expand.grid(concept_id_1 = d[[1]], concept_id_2 = d[[1]]) |> 
  janitor::clean_names() |> 
  as_tibble() |> 
  filter(concept_id_1 != concept_id_2)


old_grid <- read.delim(
  "clipboard", # existing pairs from relationships table
  col.names = c("concept_id_1", "concept_id_2")
) |> 
  janitor::clean_names() |> 
  as_tibble() |> 
  mutate(concept_combination = paste0(concept_id_1, concept_id_2))

# create grid of NEW combinations (not already included)
new_grid_filtered <- new_grid |> 
  mutate(concept_combination = paste0(concept_id_1, concept_id_2)) |> 
  filter(!concept_combination %in% old_grid$concept_combination) |> 
  select(-concept_combination)

write.csv(new_grid_filtered, "newgrid2.csv", row.names = F)


# tidy relationship matrix
d <- read.delim("clipboard")
names(d) <- c("concept_id_1", d[[1]])
relationships_tidy <- d |> 
  pivot_longer(
    cols = !concept_id_1, 
    names_to = "concept_id_2", 
    values_to = "relationship_type"
  ) |> 
  filter(!relationship_type %in% c("", NA))

write.csv(relationships_tidy, "relationships.csv", row.names = F)
