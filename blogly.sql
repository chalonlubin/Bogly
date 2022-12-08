--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5 (Homebrew)
-- Dumped by pg_dump version 14.5 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Users; Type: TABLE; Schema: public; Owner: Chalon
--

CREATE TABLE public."Users" (
    id integer NOT NULL,
    first_name character varying(100) NOT NULL,
    last_name character varying(100) NOT NULL,
    image_url text
);


ALTER TABLE public."Users" OWNER TO "Chalon";

--
-- Name: Users_id_seq; Type: SEQUENCE; Schema: public; Owner: Chalon
--

CREATE SEQUENCE public."Users_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Users_id_seq" OWNER TO "Chalon";

--
-- Name: Users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: Chalon
--

ALTER SEQUENCE public."Users_id_seq" OWNED BY public."Users".id;


--
-- Name: Users id; Type: DEFAULT; Schema: public; Owner: Chalon
--

ALTER TABLE ONLY public."Users" ALTER COLUMN id SET DEFAULT nextval('public."Users_id_seq"'::regclass);


--
-- Data for Name: Users; Type: TABLE DATA; Schema: public; Owner: Chalon
--

COPY public."Users" (id, first_name, last_name, image_url) FROM stdin;
1	Kadeem	Best	https://ichef.bbci.co.uk/news/976/cpsprodpb/3497/production/_108636431_one.jpg.webp
2	Sirius	Black	https://www.ethosvet.com/wp-content/uploads/black-cat-625x375.png
3	George 	Foreman	
4	George	GrillsALot	https://ichef.bbci.co.uk/news/976/cpsprodpb/3497/production/_108636431_one.jpg.webp
\.


--
-- Name: Users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: Chalon
--

SELECT pg_catalog.setval('public."Users_id_seq"', 4, true);


--
-- Name: Users Users_pkey; Type: CONSTRAINT; Schema: public; Owner: Chalon
--

ALTER TABLE ONLY public."Users"
    ADD CONSTRAINT "Users_pkey" PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

