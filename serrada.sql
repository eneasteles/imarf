--select * from view_serrada where jogo_fio_id = 76
--select * from producao_serrada where jogo_fio_id = 76
-- lancamentos serrada 68, 80
select * 
from 						--producao_chapas_produzidas
	producao_serrada ser,
	producao_chapas_produzidas chp,  --bloi 
	producao_maquina maq,
	producao_material mat,
	producao_bloco blo,
	producao_fio_diamantado fio,
	producao_liga liga
WHERE 
  chp.serrada_id = ser.id AND 
  maq.id = ser.maquina_id AND 
  blo.id = chp.bloco_id AND 
  mat.id = blo.material_id AND
  fio.jogo_fio = ser.jogo_fio_id AND
  liga.id = fio.liga_id 
ORDER BY ser.serrada;