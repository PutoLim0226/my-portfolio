import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

const resources = {
  en: {
    translation: {
      header: {
        about: "About",
        skills: "Skills",
        projects: "Projects"
      },
      hero: {
        title: "Hi, I'm PutoLim0226",
        subtitle: "Full-stack developer who builds fast, scalable web applications. I turn complex business problems into clean, maintainable code.",
        cta: "View Projects"
      },
      about: {
        title: "About Me",
        text: "I'm a full-stack developer passionate about performance optimization and clean architecture. With hands-on experience building web applications using React, PHP, and MySQL, I focus on delivering solutions that are both fast and maintainable. I also leverage Redis for caching and real-time data handling, and manage Linux server administration to ensure reliable, scalable deployments from development to production."
      },
      skills: {
        title: "Tech Stack"
      },
      projects: {
        title: "Featured Projects",
        github: "GitHub",
        demo: "Demo",
        items: {
          caseprofile: {
            title: "Case Profile System",
            desc: "An academic profile and case study management system with dynamic data visualization."
          },
          huiyinseh: {
            title: "Hui Yin Seh",
            desc: "A website for a Malaysian charity organization, Hui Yin Seh."
          },
          vintage: {
            title: "Vintage E-Commerce",
            desc: "A high-end e-commerce platform for vintage treasures featuring seamless cart operations."
          },
          aurora: {
            title: "Aurora Coffee",
            desc: "A glowing, immersive online coffee shop experience with interactive menus."
          },
          yhd: {
            title: "YHD Corporate Site",
            desc: "A sleek, digital transformation corporate landing page for YHD."
          },
          playyhd: {
            title: "Play YHD",
            desc: "An interactive gaming portal with vibrant neon themes and community features."
          }
        }
      },
      footer: {
        text: "© 2026 PutoLim0226 · Built with"
      }
    }
  },
  'zh-TW': {
    translation: {
      header: {
        about: "關於我",
        skills: "技能",
        projects: "作品集"
      },
      hero: {
        title: "你好，我是 PutoLim0226",
        subtitle: "全端工程師，致力於建立快速、可擴展的網頁應用程式。我將複雜的商業問題轉化為乾淨、易於維護的程式碼。",
        cta: "查看作品集"
      },
      about: {
        title: "關於我",
        text: "我是一名前端與後端皆具備經驗的全端工程師，對效能優化和乾淨的架構充滿熱情。我擁有使用 React、PHP 和 MySQL 建立網頁應用程式的實務經驗，並專注於提供快速且易於維護的解決方案。我也善用 Redis 進行快取和即時資料處理，並具備 Linux 伺服器管理能力，以確保從開發到正式環境的部署穩定且具擴展性。"
      },
      skills: {
        title: "技術堆疊"
      },
      projects: {
        title: "精選作品",
        github: "GitHub",
        demo: "展示",
        items: {
          caseprofile: {
            title: "個案基本資料系統",
            desc: "一個具備動態資料視覺化功能的學術個人檔案與個案研究管理系統。"
          },
          huiyinseh: {
            title: "慧音社",
            desc: "馬來西亞慈善團體網站 - 慧音社。"
          },
          vintage: {
            title: "復古電子商務",
            desc: "一個高端的復古珍品電子商務平台，具備流暢的購物車操作體驗。"
          },
          aurora: {
            title: "極光咖啡",
            desc: "一個發光且身歷其境的線上咖啡廳體驗，具有互動式菜單。"
          },
          yhd: {
            title: "YHD 企業網站",
            desc: "為 YHD 打造的俐落、數位轉型企業登陸頁面。"
          },
          playyhd: {
            title: "Play YHD",
            desc: "一個具有生動霓虹主題和社群功能的互動遊戲入口網站。"
          }
        }
      },
      footer: {
        text: "© 2026 PutoLim0226 · 使用建立"
      }
    }
  }
};

i18n
  .use(initReactI18next)
  .init({
    resources,
    lng: "zh-TW",
    fallbackLng: "en",
    interpolation: {
      escapeValue: false
    }
  });

export default i18n;
