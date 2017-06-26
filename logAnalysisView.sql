CREATE VIEW top_gossing AS
SELECT articles.author,articles.title,count(log.path) AS view
FROM articles JOIN log ON log.path = '/article/'||articles.slug
GROUP BY articles.author,articles.title;

CREATE VIEW daily_requests AS
SELECT date(time) as time,
       count(*) as total_views,
       sum(case when status != '200 OK' then 1.0 else 0.0 end) as total_errors
FROM log
GROUP BY date(time)
ORDER BY date(time);
