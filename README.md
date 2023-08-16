# Django Inventory

## API

Base URL: /api/v1

### Общиме поля справочников

- status
- created_date
- updated_date

### /places?nomeclature__name=стул [GET, GET :id, POST, DELETE]

- id
- name
- address

### /places/:id/groups?nomeclature__name=стул [GET, GET :id, POST, DELETE]

- id
- name
- comment

### /places/:id/groups/:id_group/instances [GET, GET :id, POST, DELETE]

- id
- nomenclature_id
- quantity
- comment

### /types [GET, GET :id, POST, DELETE]

- id
- name

### /types/:id/nomenclatures [GET, GET :id, POST, DELETE]

- id
- name
- type_id
- characteristics_values[]
  [{"id": "freq", "value": "3000MHz"},{"id": "freq", "value": "3200MHz"}]

### /types/:id/characteristics [GET, GET :id, POST, DELETE]

- id
- name

### /search?place__id=1&nomeclature__name=стул