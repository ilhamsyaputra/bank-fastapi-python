 
-- buat database
create database bank;

-- install uuid module
create extension if not exists "uuid-ossp";

-- buat table
create table nasabah (
	id uuid default uuid_generate_v4(),
	nama varchar(100) not null,
	no_hp varchar(14) not null,
	tanggal_registrasi timestamp default now(),
	
	primary key(id)
);

create table tipe_transaksi (
	tipe char(1),
	keterangan varchar(10),
	
	primary key(tipe)
);

create table rekening (
	id uuid default uuid_generate_v4() not null,
	nasabah_id uuid not null,
	no_rekening varchar(15) not null,
	saldo int not null,
	
	primary key(id),
	constraint nasabah_id
		foreign key(nasabah_id)
			references nasabah(id)
);

create table transaksi (
	id uuid default uuid_generate_v4() not null,
	rekening_id uuid not null,
	nominal int not null,
	tipe char(1) not null,
	waktu timestamp default now(),
	
	primary key(id),
	
	constraint fk_rekening_id
		foreign key(rekening_id)
			references rekening(id),
			
	constraint fk_tipe
		foreign key(tipe)
			references tipe_transaksi(tipe)
);



