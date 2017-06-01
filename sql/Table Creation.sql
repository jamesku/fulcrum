CREATE TABLE public.newsarticles
(
   "title" character varying(300),
   "article" character varying(3000), 
   "topimage" character varying(400), 
   "url" character varying(500), 
   "publish_date" date, 
   "brand" character(20), 
   "positive" double precision, 
   "negative" double precision, 
   "L2" integer, 
   "L1" integer, 
   "Neutral" integer, 
   "R1" integer, 
   "R2" integer, 
   "Score" double precision, 
   "ArticleGroupNumber" integer, 
   "PrimaryKey" integer, 
   PRIMARY KEY ("PrimaryKey")
) 
WITH (
  OIDS = FALSE
)
;

