const PILOT_TOPICS = [
  {
    id: "KNW-ID-001",
    domain: "LK01",
    title: "Cara Mengajukan Gugatan Sederhana di Pengadilan",
    summary: "Jalur pemeriksaan perdata lebih cepat untuk sengketa cidera janji atau perbuatan melawan hukum maksimal Rp500 juta (Perma No. 4 Tahun 2019), dapat didaftarkan melalui e-Court MA.",
    sourceUrl: "https://peraturan.bpk.go.id/Details/206070/perma-no-4-tahun-2019",
    sourceLabel: "Perma No. 4 Tahun 2019 (JDIH BPK)",
    status: "PENDING_HUMAN_REVIEW"
  },
  {
    id: "KNW-ID-002",
    domain: "LK03",
    title: "Pemberlakuan KUHP Nasional 2026 dan Penyesuaian Pidana",
    summary: "Mulai 2 Januari 2026, KUHP Nasional (UU No. 1 Tahun 2023) berlaku bersama UU No. 1 Tahun 2026 tentang Penyesuaian Pidana.",
    sourceUrl: "https://peraturan.bpk.go.id/Details/234935/uu-no-1-tahun-2023",
    sourceLabel: "UU No. 1 Tahun 2023 (JDIH BPK)",
    status: "PENDING_HUMAN_REVIEW"
  },
  {
    id: "KNW-ID-003",
    domain: "LK04",
    title: "Batas Usia Minimal Perkawinan (19 Tahun)",
    summary: "UU No. 16 Tahun 2019 menyamakan batas usia minimal perkawinan pria dan wanita menjadi 19 tahun.",
    sourceUrl: "https://peraturan.bpk.go.id/Details/122740/uu-no-16-tahun-2019",
    sourceLabel: "UU No. 16 Tahun 2019 (JDIH BPK)",
    status: "PENDING_HUMAN_REVIEW"
  },
  {
    id: "KNW-ID-004",
    domain: "LK05",
    title: "Hak Pekerja 2026: Batas PKWT dan Larangan Penahanan Ijazah",
    summary: "UU No. 27 Tahun 2026 (berlaku 28 Oktober 2026) mencabut UU 13/2003, melarang penahanan ijazah sebagai jaminan kerja, dan membatasi PKWT maksimal 2 tahun.",
    sourceUrl: "https://peraturan.bpk.go.id/Details/359755/uu-no-27-tahun-2026-pelindungan-ketenagakerjaan",
    sourceLabel: "UU No. 27 Tahun 2026 (JDIH BPK)",
    status: "PENDING_HUMAN_REVIEW"
  },
  {
    id: "KNW-ID-005",
    domain: "LK06",
    title: "Kriteria UMKM dan Pengelolaan Terpadu",
    summary: "PP No. 7 Tahun 2021 (Pasal 35-36 & Pasal 69) mengatur kriteria usaha mikro, kecil, dan menengah serta pengelolaan terpadu UMK.",
    sourceUrl: "https://peraturan.bpk.go.id/Details/161837/pp-no-7-tahun-2021",
    sourceLabel: "PP No. 7 Tahun 2021 (JDIH BPK)",
    status: "PENDING_HUMAN_REVIEW"
  },
  {
    id: "KNW-ID-006",
    domain: "LK07",
    title: "Pendaftaran Tanah Secara Elektronik",
    summary: "Pasal 84 PP No. 18 Tahun 2021 memungkinkan penyelenggaraan pendaftaran tanah secara elektronik.",
    sourceUrl: "https://peraturan.bpk.go.id/Details/161848/pp-no-18-tahun-2021",
    sourceLabel: "PP No. 18 Tahun 2021 (JDIH BPK)",
    status: "PENDING_HUMAN_REVIEW"
  },
  {
    id: "KNW-ID-007",
    domain: "LK08",
    title: "Hak Warga atas Standar Pelayanan Publik",
    summary: "UU No. 25 Tahun 2009 (Pasal 18 & Pasal 39) menjamin hak warga mengetahui standar pelayanan dan mengawasi pelayanan publik.",
    sourceUrl: "https://peraturan.bpk.go.id/Details/38748/uu-no-25-tahun-2009",
    sourceLabel: "UU No. 25 Tahun 2009 (JDIH BPK)",
    status: "PENDING_HUMAN_REVIEW"
  },
  {
    id: "KNW-ID-008",
    domain: "LK09",
    title: "Hak Dasar Konsumen",
    summary: "Pasal 4 UU No. 8 Tahun 1999 melindungi hak konsumen atas keamanan, informasi jujur, dan penyelesaian sengketa.",
    sourceUrl: "https://peraturan.bpk.go.id/Details/45288/uu-no-8-tahun-1999",
    sourceLabel: "UU No. 8 Tahun 1999 (JDIH BPK)",
    status: "PENDING_HUMAN_REVIEW"
  },
  {
    id: "KNW-ID-009",
    domain: "LK10",
    title: "Bantuan Hukum Gratis bagi Warga Tidak Mampu",
    summary: "UU No. 16 Tahun 2011 menjamin pendampingan hukum gratis melalui Organisasi Bantuan Hukum (OBH) terakreditasi BPHN.",
    sourceUrl: "https://peraturan.bpk.go.id/Details/39234/uu-no-16-tahun-2011",
    sourceLabel: "UU No. 16 Tahun 2011 (JDIH BPK)",
    status: "PENDING_HUMAN_REVIEW"
  },
  {
    id: "KNW-ID-010",
    domain: "LK11",
    title: "Hak Subjek Data Pribadi (3x24 Jam)",
    summary: "Pasal 30 UU No. 27 Tahun 2022 mewajibkan pengendali data memperbaiki ketidakakuratan data pribadi maksimal 3x24 jam.",
    sourceUrl: "https://peraturan.bpk.go.id/Details/229798/uu-no-27-tahun-2022",
    sourceLabel: "UU No. 27 Tahun 2022 (JDIH BPK)",
    status: "PENDING_HUMAN_REVIEW"
  }
];

function renderTopics() {
  const query = document.getElementById("search-input").value.toLowerCase();
  const domain = document.getElementById("domain-filter").value;
  const container = document.getElementById("topics-list");

  const filtered = PILOT_TOPICS.filter((item) => {
    const matchDomain = domain === "ALL" || item.domain === domain;
    const matchQuery =
      item.title.toLowerCase().includes(query) ||
      item.summary.toLowerCase().includes(query);
    return matchDomain && matchQuery;
  });

  if (filtered.length === 0) {
    container.innerHTML = "<p>Tidak ada topik yang cocok dengan pencarian Anda.</p>";
    return;
  }

  container.innerHTML = filtered
    .map(
      (item) => `
      <article class="card">
        <span class="badge">${item.domain}</span>
        <span class="badge badge-pending">${item.status}</span>
        <h3>${item.title}</h3>
        <p>${item.summary}</p>
        <p><a href="${item.sourceUrl}" target="_blank" rel="noopener noreferrer">${item.sourceLabel}</a></p>
      </article>`
    )
    .join("");
}

document.getElementById("search-input").addEventListener("input", renderTopics);
document.getElementById("domain-filter").addEventListener("change", renderTopics);
renderTopics();
